import numpy as np

def reward_function(params):

  # --------------------------- Weights --------------------------- #

  steering_weight = 55
  center_weight = 30
  speed_weight = 15

  # ---------------------- Off-track Penalty ---------------------- #

  # Penalize if off track
  if not params['all_wheels_on_track']:
    return 1e-3
  
  # --------------------------- Params --------------------------- #

  speed = params['speed']
  steering_angle = params['steering_angle']
  heading = params['heading']
  track_width = params['track_width']
  distance_from_center = params['distance_from_center']
  closest_waypoints = params['closest_waypoints']
  waypoints = np.array(params['waypoints'])
  
  # --------------------------- Heading --------------------------- #

  # I don't think there's really any benefit to rewarding separately for
  # steering and heading, so I will omit the heading reward

  # calculate track direction angle
  track_vector = waypoints[closest_waypoints[1]]-waypoints[closest_waypoints[0]]
  track_direction = np.arctan2(track_vector[1], track_vector[0])*180/np.pi

  # reward if heading direction is the same as track direction
  # heading_difference = abs(track_direction-heading)
  # heading_difference = heading_difference if heading_difference < 180 else 360-heading_difference

  # # when heading angle difference is 20, the reward is 1/e~0.37
  # heading_reward = np.exp(-0.0025*heading_difference**2) if heading_difference < 45 else 0

  # --------------------------- Steering --------------------------- #

  # reward if steering direction is the same as track direction
  steering_direction = steering_angle+heading
  steering_difference = abs(track_direction-steering_direction)
  steering_difference = steering_difference if steering_difference < 180 else 360-steering_difference

  # when steering difference is 16, the reward is 1/e~0.37
  steering_reward = np.exp(-0.004*steering_difference**2) if steering_difference < 30 else 0

  # --------------------------- Center --------------------------- #

  # reward if close to center line

  # when at 50% of the track width, the reward is 1/e~0.37
  center_reward = np.exp(-16*(distance_from_center/track_width)**2) if distance_from_center < track_width/2 else 0

  # --------------------------- Speed --------------------------- #

  # reward for speed
  ideal_speed = 0.67

  # when speed deviates from ideal_speed by 0.5, reward is 1/e~0.37
  speed_reward = np.exp(-4*(ideal_speed-speed)**2) if speed > 0 else 0

  # --------------------------- Total --------------------------- #
  
  # print('track_direction:', track_direction)
  # print('heading:', heading)
  # print('steering_difference:', steering_difference)
  # print('steering_reward:', steering_reward)
  # print('center_reward:', center_reward)
  # print('speed_reward:', speed_reward)

  reward = steering_weight*steering_reward + center_weight*center_reward + speed_weight*speed_reward
  reward = reward if reward > 1e-3 else 1e-3
  print('rewards:', steering_reward, center_reward, speed_reward, reward)
  print('car stats:', params['x'], params['y'], speed, steering_angle, heading)
  return float(reward)
