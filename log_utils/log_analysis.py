import os
import pickle
import numpy as np
import statistics
import matplotlib.pyplot as plt

dir_name = os.path.dirname(os.path.abspath(__file__))
pickled_file_name = 'ace-reward-function-testing-4'

def loadData(pickled_file_name):
  file = open('%s/pickles/%s' % (dir_name, pickled_file_name), 'rb')
  episodes = pickle.load(file)
  file.close()
  return episodes

# 0: steering reward
# 1: heading reward
# 2: center reward
# 3: speed reward
# 4: progress reward
# 5: total reward
# 6: position
# 7: speed
# 8: steering angle
# 9: heading
# 10: closest_waypoints
# 11: distance from center
# 12: track length
# 13: steps
# 14: progress
# 15: track name
# 16: min speed
# 17: max speed
# 18: track direction
# 19: steering difference
# 20: heading difference
# 21: distance from race line
# 22: track_fraction
# 23: speed difference
# 24: lookahead_points
# 25: penalty


reward_function_testing_data = loadData(f'{pickled_file_name}.pickle')

def countPenalties(episodes):
  penalties = {
    'none': 0,
    'off_track': 0,
    'off_steering': 0,
    'off_heading': 0,
    'off_center': 0,
    'off_speed': 0,
  }
  for episode in episodes:
    for step_log in episode:
      if (step_log[24] == 'none'): penalties['none'] += 1
      if (step_log[10] > 1.067 / 2): penalties['off_track'] += 1
      if (step_log[18] > 20): penalties['off_steering'] += 1
      if (step_log[19] > 30): penalties['off_heading'] += 1
      if (step_log[21] > 0.75): penalties['off_center'] += 1
      if (step_log[22] > 1.5): penalties['off_speed'] += 1
      
  return penalties

def plotDifferences(episodes):
  steering_diffs = []
  heading_diffs = []
  track_fraction_diffs = []
  speed_diffs = []

  for episode in episodes:
    for step_log in episode:
      steering_diffs.append(step_log[18])
      heading_diffs.append(step_log[19])
      track_fraction_diffs.append(step_log[21])
      speed_diffs.append(step_log[22])
  
  print('steering', statistics.stdev(steering_diffs))
  print('heading', statistics.stdev(heading_diffs))
  print('track_fraction', statistics.stdev(track_fraction_diffs))
  print('speed', statistics.stdev(speed_diffs))

  def saveHistogram(diffs, bins, bound, name):
    plt.hist(diffs, bins, [0, bound])
    plt.savefig(f'{dir_name}/{pickled_file_name}_{name}.png')
    plt.clf()

  saveHistogram(steering_diffs, 30, 60, 'steering_diffs')
  saveHistogram(heading_diffs, 30, 60, 'heading_diffs')
  saveHistogram(track_fraction_diffs, 30, 1.5, 'track_fraction_diffs')
  saveHistogram(speed_diffs, 30, 4, 'speed_diffs')

print(countPenalties(reward_function_testing_data[:int(len(reward_function_testing_data)/2)]))
print(countPenalties(reward_function_testing_data[int(len(reward_function_testing_data)/2):]))
print(countPenalties(reward_function_testing_data))
penalties = countPenalties(reward_function_testing_data)
total = 0
for key in penalties:
  total += penalties[key]
for key in penalties:
  penalties[key] /= total
print(penalties)
print('# episodes in first half', sum([len(episode) for episode in reward_function_testing_data[:int(len(reward_function_testing_data)/2)]]))
print('# episodes in second half', sum([len(episode) for episode in reward_function_testing_data[int(len(reward_function_testing_data)/2):]]))

# plotDifferences(reward_function_testing_data)

# maybe have 1.5 stddevs

def plotSteeringVsSpeed(episodes):
  speed = []
  steering = []

  for episode in episodes:
    for step_log in episode:
      speed.append(step_log[6])
      steering.append(step_log[7])

  plt.scatter(steering, speed)
  plt.savefig(f'{dir_name}/{pickled_file_name}_steeringVspeed.png')
  plt.clf()

