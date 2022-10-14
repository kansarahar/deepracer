# --------------------------- Info --------------------------- #
# This is a tool used to plot the processed track information
#
# Example: python plot_track.py --track_name reinvent2018
# 
# Type `python plot_track.py --help` for more information
#
# --------------------------- Args --------------------------- #

import os
import sys
import argparse
import numpy as np
import matplotlib.pyplot as plt

dir_name = os.path.dirname(os.path.abspath(__file__))

parser = argparse.ArgumentParser(description='A tool used to process waypoints obtained from a .npy file')
parser.add_argument('--track_name', type=str, nargs=1, help='REQUIRED - name of the track, example: reinvent2018', required=True)
parser.add_argument('--number', action='store_true', help='OPTIONAL - displays the number of the waypoint next to every 10 waypoints')
parser.add_argument('--meter', action='store_true', help='OPTIONAL - displays the meters traveled across the track')
parser.add_argument('--line', action='store_true', help='OPTIONAL - plot as line graph instead of scatter')

args = parser.parse_args()

track_name, show_numbers, show_meters, line_graph = args.track_name[0], args.number, args.meter, args.line

# ------------------------ Plot Main ------------------------- #

# Get points from .npy files
points = np.load('%s/../tracks/track_points/%s.npy' % (dir_name, track_name))
colors = {
  'waypoints': '#6d6dff',
  'innerpoints': '#ff6d6d',
  'outerpoints': '#6dff6d',
  'metermarker': '#ffa500',
  'indexmarker': '#000000'
}

if not line_graph:
  # Plot waypoints as scatter
  for i in range(len(points)):
    plt.scatter(points[i][0], points[i][1], c=colors['waypoints'])
    plt.scatter(points[i][2], points[i][3], c=colors['innerpoints'])
    plt.scatter(points[i][4], points[i][5], c=colors['outerpoints'])
else:
  # Plot waypoints as lines
  plt.plot([point[0] for point in points], [point[1] for point in points], c=colors['waypoints'])
  plt.plot([point[2] for point in points], [point[3] for point in points], c=colors['innerpoints'])
  plt.plot([point[4] for point in points], [point[5] for point in points], c=colors['outerpoints'])

# ----------------------- Plot Options ----------------------- #
waypoints = np.array([[points[i][0], points[i][1]] for i in range(len(points))])
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

plt.axis('scaled')
os.makedirs('%s/plots/tracks' % os.path.abspath(os.path.join(dir_name, '..')), exist_ok=True)
plt.savefig('%s/../plots/tracks/%s.png' % (dir_name, track_name))
print('Image saved as plots/tracks/%s.png' % track_name)
