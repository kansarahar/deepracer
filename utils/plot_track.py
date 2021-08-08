# --------------------------- Info --------------------------- #
# This is a tool used to plot the processed track information
#
# Example: python plot_track.py --track_name reinvent2018
# 
# Type `python plot_track.py --help` for more information
#
# --------------------------- Args --------------------------- #

import os
import argparse
import numpy as np
import matplotlib.pyplot as plt

dir_name = os.path.dirname(os.path.abspath(__file__))

parser = argparse.ArgumentParser(description='A tool used to process waypoints obtained from a .npy file')
parser.add_argument('--track_name', type=str, nargs=1, help='REQUIRED - name of the track, example: reinvent2018', required=True)
parser.add_argument('--img_name', type=str, nargs=1, help='OPTIONAL - name of the output image, default: track.png', default=['track.png'])
parser.add_argument('--number', action='store_true', help='OPTIONAL - displays the number of the waypoint next to every 10 waypoints')
parser.add_argument('--meter', action='store_true', help='OPTIONAL - displays the meters traveled across the track')
parser.add_argument('--line', action='store_true', help='OPTIONAL - plot as line graph instead of scatter')

args = parser.parse_args()

track_name, img_name, show_numbers, show_meters, line_graph = args.track_name[0], args.img_name[0], args.number, args.meter, args.line

# ------------------------ Plot Main ------------------------- #

# Get points from .npy files
waypoints, rightpoints, leftpoints = [np.load('%s/../tracks/track_%s/%s.npy' % (dir_name, points_set, track_name)) for points_set in ['waypoints', 'rightpoints', 'leftpoints']]
waypoints, rightpoints, leftpoints = np.array(waypoints), np.array(rightpoints), np.array(leftpoints)
colors = {
  'waypoints': '#6d6dff',
  'rightpoints': '#ff6d6d',
  'leftpoints': '#6dff6d',
  'metermarker': '#ffa500',
  'indexmarker': '#000000'
}

if not line_graph:
  # Plot waypoints as scatter
  for i in range(len(waypoints)):
    plt.scatter(waypoints[i][0], waypoints[i][1], c=colors['waypoints'])
    plt.scatter(rightpoints[i][0], rightpoints[i][1], c=colors['rightpoints'])
    plt.scatter(leftpoints[i][0], leftpoints[i][1], c=colors['leftpoints'])
else:
  # Plot waypoints as lines
  plt.plot([point[0] for point in waypoints], [point[1] for point in waypoints], c=colors['waypoints'])
  plt.plot([point[0] for point in rightpoints], [point[1] for point in rightpoints], c=colors['rightpoints'])
  plt.plot([point[0] for point in leftpoints], [point[1] for point in leftpoints], c=colors['leftpoints'])

# ----------------------- Plot Options ----------------------- #

total_dist = 0
marker_dist = 0
for i in range(len(waypoints)):
  if show_numbers:
    if i % 10 == 0:
      plt.text(waypoints[i][0] * 1.02, waypoints[i][1] * 1.02 , i, fontsize=10)
      plt.scatter(waypoints[i][0], waypoints[i][1], c=colors['indexmarker'])
  if show_meters and i+1 < len(waypoints):
    if marker_dist >= 1 or i == 0:
      marker_dist -= 1 if i > 0 else 0
      plt.text(waypoints[i][0] * 1.02, waypoints[i][1] * 1.02, '%sm' % int(total_dist), fontsize=10)
      plt.scatter(waypoints[i][0], waypoints[i][1], c=colors['metermarker'])
    total_dist += np.linalg.norm(waypoints[i+1]-waypoints[i])
    marker_dist += np.linalg.norm(waypoints[i+1]-waypoints[i])

# ------------------------ Save Image ------------------------ #

os.makedirs('%s/plots' % os.path.abspath(os.path.join(dir_name, '..')), exist_ok=True)
plt.savefig('%s/../plots/%s' % (dir_name, img_name))
print('Image saved as %s' % img_name)
