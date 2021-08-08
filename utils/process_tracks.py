# --------------------------- Info --------------------------- #
# This is a tool used to process waypoints that were saved as .npy files. 
# It will create inner and outer points along the track
#
# Example: python process_tracks.py --track_name reinvent2018
# 
# Type `python process_tracks.py --help` for more help

import os
import json
import numpy as np

tracks = {}
dir_name = os.path.dirname(os.path.abspath(__file__))
with open('%s/../tracks/tracks.json' % dir_name) as json_file:
  tracks = json.load(json_file)

for track_name in tracks:

  track_width = tracks[track_name]['width']
  waypoints = np.array(tracks[track_name]['waypoints'])

  if (track_width <= 0):
    print('Track width for %s track is <= 0, resolve in tracks.json before continuing' % track_width)

  # ------------- Calculate Inner and Outer Points ------------- #

  rightpoints = np.zeros(waypoints.shape)
  leftpoints = np.zeros(waypoints.shape)
  for i in range(len(waypoints)):
    curr_point = i
    next_point = i+1 if i+1 < len(waypoints) else 0
    prev_point = i-1 if i-1 >= 0 else len(waypoints)-1
    direction = waypoints[next_point]-waypoints[prev_point]
    direction = direction/np.linalg.norm(direction)
    perp = np.array([direction[1], -1*direction[0]])
    rightpoints[i] = waypoints[i] + perp*track_width/2
    leftpoints[i] = waypoints[i] - perp*track_width/2

  # --------------------------- Save --------------------------- #

  path = os.path.abspath(os.path.join(dir_name, '..', 'tracks'))
  os.makedirs('%s/track_waypoints' % path, exist_ok=True)
  os.makedirs('%s/track_rightpoints' % path, exist_ok=True)
  os.makedirs('%s/track_leftpoints' % path, exist_ok=True)

  np.save(os.path.join(path, 'track_waypoints', '%s.npy' % track_name), waypoints)
  print('Saved waypoints for %s track under %s' % (track_name, os.path.relpath(path)))
  
  np.save(os.path.join(path, 'track_rightpoints', '%s.npy' % track_name), rightpoints)
  print('Saved rightpoints for %s track under %s' % (track_name, os.path.relpath(path)))
  
  np.save(os.path.join(path, 'track_leftpoints', '%s.npy' % track_name), leftpoints)
  print('Saved leftpoints for %s track under %s' % (track_name, os.path.relpath(path)))
