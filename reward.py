import numpy as np

def reward_function(params):

  # ----------------------------------------------------- #

  heading_weight = 35
  steering_weight = 20
  center_weight = 35
  speed_weight = 10

  # ----------------------------------------------------- #

  # Penalize if off track
  if not params['all_wheels_on_track']:
    return 1e-3
  
  # ----------------------------------------------------- #

  speed = params['speed']
  steering_angle = params['steering_angle']
  heading_direction = params['heading']
  track_width = params['track_width']
  distance_from_center = params['distance_from_center']
  closest_waypoints = params['closest_waypoints']
  waypoints = np.array(params['waypoints'])
  
  # ----------------------------------------------------- #

  # calculate track direction angle
  track_vector = waypoints[closest_waypoints[1]]-waypoints[closest_waypoints[0]]
  track_direction = np.arctan2(track_vector[1], track_vector[0])*180/np.pi


  # reward if heading direction is the same as track direction
  heading_difference = abs(track_direction-heading_direction)
  heading_difference = heading_difference if heading_difference < 180 else 360-heading_difference

  heading_reward = ((45-heading_difference)/45)**2 if heading_difference < 45 else 0
  heading_reward = heading_reward if heading_reward < 1 else 1

  # ----------------------------------------------------- #

  # reward if steering direction is the same as track direction
  steering_direction = steering_angle+heading_direction
  steering_direction = steering_direction if steering_direction < 180 else 360-steering_direction
  steering_difference = abs(track_direction-(steering_angle+heading_direction))
  steering_difference = steering_difference if steering_difference < 180 else 360-steering_difference

  steering_reward = ((45-steering_difference)/45)**2 if steering_difference < 45 else 0
  steering_reward = steering_reward if steering_reward < 1 else 1

  # ----------------------------------------------------- #

  # reward if close to center line
  center_reward = 1-distance_from_center/(track_width/2)
  center_reward = center_reward if distance_from_center < track_width/2 else 0
  center_reward = center_reward if center_reward < 1 else 1

  # ----------------------------------------------------- #

  # reward if higher speed
  speed_reward = speed/5
  speed_reward = speed_reward if speed_reward < 1 else 1

  # print('track_direction:', track_direction)
  # print('heading_direction:', heading_direction)
  # print('heading_difference:', heading_difference)
  # print('steering_difference:', steering_difference)
  # print('heading_reward:', heading_reward)
  # print('steering_reward:', steering_reward)
  # print('center_reward:', center_reward)
  # print('speed_reward:', speed_reward)

  # ----------------------------------------------------- #

  reward = heading_weight*heading_reward + steering_weight*steering_reward + center_weight*center_reward + speed_weight*speed_reward
  reward = reward if reward > 0 else 1e-3
  print('rewards:', heading_reward, steering_reward, center_reward, speed_reward, reward)
  return float(reward)