import os
import sys
import copy
import argparse
import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import Point, Polygon
from shapely.geometry.polygon import LinearRing, LineString

parser = argparse.ArgumentParser(description='A tool used to process waypoints obtained from a .npy file')
parser.add_argument('--track_name', type=str, nargs=1, help='REQUIRED - Name of the track, example: reinvent2018', required=True)
parser.add_argument('--xi_iterations', dest='xi_iterations', type=int, default=4, help='OPTIONAL - Number of times to iterate each new race line point. Keep this at 3-8 for best balance of performance and desired result. (default: 4)')
parser.add_argument('--line_iterations', dest='line_iterations', type=int, default=500, help='OPTIONAL - Number of times to scan the entire race track to iterate. 500 will get a good start, 1500 will be closer to optimal result. (default: 500)')

args = parser.parse_args()
track_name, xi_iterations, line_iterations = args.track_name[0], args.xi_iterations, args.line_iterations

# Get points from .npy files
points = np.load('%s/../tracks/track_points/%s.npy' % (dir_name, track_name))


# ------------------------ Calculation Functions ------------------------- #

# all functions taken directly from https://github.com/cdthompson/deepracer-k1999-race-lines/blob/master/Race-Line-Calculation.ipynb

def menger_curvature(pt1, pt2, pt3, atol=1e-3):

  vec21 = np.array([pt1[0]-pt2[0], pt1[1]-pt2[1]])
  vec23 = np.array([pt3[0]-pt2[0], pt3[1]-pt2[1]])

  norm21 = np.linalg.norm(vec21)
  norm23 = np.linalg.norm(vec23)

  theta = np.arccos(np.dot(vec21, vec23)/(norm21*norm23))
  if np.isclose(theta-np.pi, 0.0, atol=atol):
    theta = 0.0

  dist13 = np.linalg.norm(vec21-vec23)

  return 2*np.sin(theta) / dist13

def improve_race_line(old_line, inner_border, outer_border):
  '''Use gradient descent, inspired by K1999, to find the racing line'''
  # start with the center line
  new_line = copy.deepcopy(old_line)
  ls_inner_border = Polygon(inner_border)
  ls_outer_border = Polygon(outer_border)
  for i in range(0,len(new_line)):
    xi = new_line[i]
    npoints = len(new_line)
    prevprev = (i - 2 + npoints) % npoints
    prev = (i - 1 + npoints) % npoints
    nexxt = (i + 1 + npoints) % npoints
    nexxtnexxt = (i + 2 + npoints) % npoints
    #print("%d: %d %d %d %d %d" % (npoints, prevprev, prev, i, nexxt, nexxtnexxt))
    ci = menger_curvature(new_line[prev], xi, new_line[nexxt])
    c1 = menger_curvature(new_line[prevprev], new_line[prev], xi)
    c2 = menger_curvature(xi, new_line[nexxt], new_line[nexxtnexxt])
    target_ci = (c1 + c2) / 2
    #print("i %d ci %f target_ci %f c1 %f c2 %f" % (i, ci, target_ci, c1, c2))

    # Calculate prospective new track position, start at half-way (curvature zero)
    xi_bound1 = copy.deepcopy(xi)
    xi_bound2 = ((new_line[nexxt][0] + new_line[prev][0]) / 2.0, (new_line[nexxt][1] + new_line[prev][1]) / 2.0)
    p_xi = copy.deepcopy(xi)
    for j in range(0,xi_iterations):
      p_ci = menger_curvature(new_line[prev], p_xi, new_line[nexxt])
      #print("i: {} iter {} p_ci {} p_xi {} b1 {} b2 {}".format(i,j,p_ci,p_xi,xi_bound1, xi_bound2))
      if np.isclose(p_ci, target_ci):
        break
      if p_ci < target_ci:
        # too flat, shrinking track too much
        xi_bound2 = copy.deepcopy(p_xi)
        new_p_xi = ((xi_bound1[0] + p_xi[0]) / 2.0, (xi_bound1[1] + p_xi[1]) / 2.0)
        if Point(new_p_xi).within(ls_inner_border) or not Point(new_p_xi).within(ls_outer_border):
            xi_bound1 = copy.deepcopy(new_p_xi)
        else:
            p_xi = new_p_xi
      else:
        # too curved, flatten it out
        xi_bound1 = copy.deepcopy(p_xi)
        new_p_xi = ((xi_bound2[0] + p_xi[0]) / 2.0, (xi_bound2[1] + p_xi[1]) / 2.0)

        # If iteration pushes the point beyond the border of the track,
        # just abandon the refinement at this point.  As adjacent
        # points are adjusted within the track the point should gradually
        # make its way to a new position.  A better way would be to use
        # a projection of the point on the border as the new bound.  Later.
        if Point(new_p_xi).within(ls_inner_border) or not Point(new_p_xi).within(ls_outer_border):
          xi_bound2 = copy.deepcopy(new_p_xi)
        else:
          p_xi = new_p_xi
    new_xi = p_xi
    # New point which has mid-curvature of prev and next points but may be outside of track
    #print((new_line[i], new_xi))
    new_line[i] = new_xi
  return new_line


# ------------------------ Race Line Calculation ------------------------- #

center_line = np.array(points[:, 0:2])
inner_line = np.array(points[:, 2:4])
outer_line = np.array(points[:, 4:6])

race_line = copy.deepcopy(center_line[:])
print(len(center_line), len(race_line))
for i in range(line_iterations):
  race_line = improve_race_line(race_line, inner_line, outer_line)
  if i % 100 == 0:
    print('Iteration %s' % i)


# ------------------------ Save and Plot Optimal Path ------------------------- #

dir_name = os.path.dirname(os.path.abspath(__file__))
path = os.path.abspath(os.path.join(dir_name, '..', 'tracks'))
os.makedirs('%s/optimal_track_waypoints' % path, exist_ok=True)

np.save(os.path.join(path, 'optimal_track_waypoints', '%s.npy' % track_name), race_line)
print('Saved optimal track waypoints for %s track under %s' % (track_name, os.path.relpath(path)))

for i in range(len(points)):
  plt.scatter(inner_line[i][0], inner_line[i][1], c='red')
  plt.scatter(center_line[i][0], center_line[i][1], c='green')
  plt.scatter(outer_line[i][0], outer_line[i][1], c='blue')
  plt.scatter(race_line[i][0], race_line[i][1], c='black')

os.makedirs('%s/plots' % os.path.abspath(os.path.join(dir_name, '..')), exist_ok=True)
plt.savefig('%s/../plots/%s_optimal.png' % (dir_name, track_name))
print('Image saved as %s_optimal.png' % track_name)














