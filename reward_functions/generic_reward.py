import numpy as np

EXPECTED_SLOW_COMPLETION_TIME = 30
EXPECTED_FASTEST_COMPLETION_TIME = 15
EXPECTED_TOTAL_REWARD_PER_LENGTH = 175

def reward_function(params):

  MIN_REWARD = 1e-3
  STEPS_PER_SECOND = 15

  # --------------------------- Weights --------------------------- #

  STEERING_WEIGHT = 55
  CENTER_WEIGHT = 30
  SPEED_WEIGHT = 15
  PROGRESS_WEIGHT = 1

  # ----------------------- Off-track Penalty ----------------------- #
  
  if not params['all_wheels_on_track']:
    return MIN_REWARD
  
  # --------------------------- Params --------------------------- #

  speed = params['speed']
  steering_angle = params['steering_angle']
  heading = params['heading']
  track_width = params['track_width']
  distance_from_center = params['distance_from_center']
  closest_waypoints = params['closest_waypoints']
  waypoints = np.array(params['waypoints'])
  track_length = params['track_length']
  progress = params['progress']
  steps = params['steps']
  x = params['x']
  y = params['y']
  
  # --------------------------- Direction --------------------------- #

  # calculate track direction angle
  track_vector = waypoints[closest_waypoints[1]]-waypoints[closest_waypoints[0]]
  track_direction = np.arctan2(track_vector[1], track_vector[0])*180/np.pi

  # reward if steering direction is the same as track direction
  steering_direction = steering_angle+heading
  steering_difference = abs(track_direction-steering_direction)
  steering_difference = steering_difference if steering_difference < 180 else 360-steering_difference

  # punish hard if heading direction is way off
  heading_difference = abs(track_direction-heading)
  heading_difference = heading_difference if heading_difference < 180 else 360-heading_difference
  if heading_difference > 20:
    return MIN_REWARD

  # when steering difference is 8, the reward is 1/e~0.37
  steering_reward = np.exp(-(steering_difference/10)**2) if steering_difference < 15 else 0

  # --------------------------- Center --------------------------- #

  # fraction of the distance to the center line
  track_fraction = 2 * distance_from_center / track_width

  # punish hard if too far from center line
  if track_fraction > 0.6:
    return MIN_REWARD

  # when at 30% of the track width, the reward is 1/e~0.37
  center_reward = np.exp(-(track_fraction/0.30)**2) if track_fraction < 0.5 else 0

  # --------------------------- Speed --------------------------- #

  # difference in expected speed vs actual speed
  ideal_speed = 0.67
  speed_difference = ideal_speed - speed

  # punish hard if too slow
  if speed_difference > 1.5:
    return MIN_REWARD

  # when speed deviates from ideal_speed by 0.25, reward is 1/e~0.37
  speed_reward = np.exp(-(speed_difference/0.25)**2) if speed > 0 else 0

  # --------------------------- Progress --------------------------- #

  slow_total_steps = EXPECTED_SLOW_COMPLETION_TIME * STEPS_PER_SECOND
  fastest_total_steps = EXPECTED_FASTEST_COMPLETION_TIME * STEPS_PER_SECOND
  progress_reward = 0
  if (progress == 100):
    # interpolate between slow and fast steps
    expected_total_reward = EXPECTED_TOTAL_REWARD_PER_LENGTH * track_length
    progress_reward = expected_total_reward * (steps - slow_total_steps) / (fastest_total_steps - slow_total_steps)
    progress_reward = progress_reward if progress_reward > 0 else 0

  # --------------------------- Total --------------------------- #

  reward = STEERING_WEIGHT*steering_reward + CENTER_WEIGHT*center_reward + SPEED_WEIGHT*speed_reward + PROGRESS_WEIGHT*progress_reward
  reward = reward if reward > MIN_REWARD else MIN_REWARD
  print(f'REWARDS: steering_reward({steering_reward}), center_reward({center_reward}), speed_reward({speed_reward}), total_reward({reward})')
  print(f'PARAMS: position({x}, {y}), speed({speed}), steering_angle({steering_angle}), heading({heading}), track_direction({track_direction}), progress({progress})')
  return float(reward)
