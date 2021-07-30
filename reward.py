import numpy as np
import math

def reward_function(params):

  # ----------------------------------------------------- #

  # Penalize if off track
  if not params['all_wheels_on_track']:
    return 1e-3
  
  # ----------------------------------------------------- #

  speed = params['speed']
  steering_angle = params['steering_angle']
  heading = params['heading']
  waypoints = np.array(params['waypoints'])
  closest_waypoints = np.array(params['closest_waypoints'])

  # calculate track direction unit vector
  track_direction = waypoints[closest_waypoints[1]]-waypoints[closest_waypoints[0]]
  track_direction = track_direction/np.linalg.norm(track_direction)
  
  # ----------------------------------------------------- #

  # reward if heading direction is the same as track direction
  heading_direction = np.array([np.cos(heading), np.sin(heading)])
  heading_angular_difference = np.arccos(track_direction.dot(heading_direction))*180/np.pi
  heading_reward = ((45-heading_angular_difference)/45)**2 if heading_angular_difference < 45 else 0

  # ----------------------------------------------------- #

  # reward if steering direction is the same as track direction
  steering_direction = np.array([np.cos(heading+steering_angle), np.sin(heading+steering_angle)])
  steering_angular_difference = np.arccos(track_direction.dot(steering_direction))*180/np.pi
  steering_reward = ((45-steering_angular_difference)/45)**2 if steering_angular_difference < 45 else 0

  # ----------------------------------------------------- #

  print('track_direction: %s' % track_direction)
  print('heading_direction: %s' % heading_direction)
  print('heading_angular_difference: %s' % heading_angular_difference)
  print('heading_reward: %s' % heading_reward)

  # ----------------------------------------------------- #

  reward = heading_reward*speed*steering_angle*steering_reward
  return reward