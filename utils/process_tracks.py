# --------------------------- Info --------------------------- #

# This is a tool used to process waypoints from the tracks.json file
# It will create right and left points along the track and save them as .npy files
#
# Example: python process_tracks.py --track_name reinvent2018
# 
# Type `python process_tracks.py --help` for more help

import os
import sys
import json
import numpy as np
from track_data import track_data

for track_name in track_data:

  track_width = track_data[track_name]['width']
  waypoints = np.array(track_data[track_name]['waypoints'])

  if (track_width <= 0):
    print('Track width for %s track is <= 0, resolve in tracks.json before continuing' % track_width)

  # -------------- Calculate Right and Left Points -------------- #
  
  points = np.zeros((len(waypoints), 6));
  for i in range(len(waypoints)):
    curr_point = i
    next_point = i+1 if i+1 < len(waypoints) else 0
    prev_point = i-1 if i-1 >= 0 else len(waypoints)-1
    direction = waypoints[next_point]-waypoints[prev_point]
    direction = direction/np.linalg.norm(direction)
    perp = np.array([direction[1], -1*direction[0]])

    # points contains waypoints, innerpoints, and outerpoints
    points[i][0:2] = waypoints[i]
    points[i][2:4] = waypoints[i] - perp*(track_width - 0.2)/2 # -0.2 to account for car width
    points[i][4:6] = waypoints[i] + perp*(track_width - 0.2)/2
  

  # --------------------------- Save --------------------------- #
  
  dir_name = os.path.dirname(os.path.abspath(__file__))
  path = os.path.abspath(os.path.join(dir_name, '..', 'tracks'))
  os.makedirs('%s/track_points' % path, exist_ok=True)

  np.save(os.path.join(path, 'track_points', '%s.npy' % track_name), points)
  print('Saved points for %s track under %s' % (track_name, os.path.relpath(path)))
