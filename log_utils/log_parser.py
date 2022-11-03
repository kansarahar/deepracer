import os
import sys
import copy
import pickle

log_name = 'ace-reward-function-testing-4.log'
dir_name = os.path.dirname(os.path.abspath(__file__))
path = os.path.abspath(os.path.join(dir_name, log_name))

file = open(path, 'r')
file_lines = file.readlines()
episodes = []
episode = []
step_log = []

# rewards = [] # [steering, heading, center, speed, progress]
# line_num = 0
# while line_num < len(file_lines):
#   line = file_lines[line_num]
#   if (line == 'Reset agent finished\n' or line_num == len(file_lines)-1):
#     if (episode): episodes.append(copy.deepcopy(episode))
#     episode = []
#   if (line == '=============== <REWARDS> ===============\n'):
#     rewards.append(float(file_lines[line_num+1][17: -1])) # steering reward
#     rewards.append(float(file_lines[line_num+2][16: -1])) # heading reward
#     rewards.append(float(file_lines[line_num+3][15: -1])) # center reward
#     rewards.append(float(file_lines[line_num+4][14: -1])) # speed reward
#     rewards.append(float(file_lines[line_num+16][10: -1])) # progress
#     episode.append(copy.deepcopy(rewards))
#     rewards = []
#     line_num += 16

#   line_num += 1

line_num = 0
while line_num < len(file_lines):
  line = file_lines[line_num]
  if (line == 'Reset agent finished\n' or line_num == len(file_lines)-1):
    if (episode): episodes.append(copy.deepcopy(episode))
    episode = []
  if (line == '=============== <REWARDS> ===============\n'):
    step_log.append(float(file_lines[line_num+1][17: -1])) # steering reward
    step_log.append(float(file_lines[line_num+2][16: -1])) # heading reward
    step_log.append(float(file_lines[line_num+3][15: -1])) # center reward
    step_log.append(float(file_lines[line_num+4][14: -1])) # speed reward
    step_log.append(float(file_lines[line_num+5][17: -1])) # progress reward
    step_log.append(file_lines[line_num+8][10: -1]) # position
    step_log.append(float(file_lines[line_num+9][7: -1])) # speed
    step_log.append(float(file_lines[line_num+10][16: -1])) # steering angle
    step_log.append(float(file_lines[line_num+11][9: -1])) # heading
    step_log.append(file_lines[line_num+12][19: -1]) # closest_waypoints
    step_log.append(float(file_lines[line_num+13][22: -1])) # distance from center
    step_log.append(float(file_lines[line_num+14][14: -1])) # track length
    step_log.append(float(file_lines[line_num+15][7: -1])) # steps
    step_log.append(float(file_lines[line_num+16][10: -1])) # progress
    step_log.append(file_lines[line_num+19][12: -1]) # track name
    step_log.append(float(file_lines[line_num+20][11: -1])) # min speed
    step_log.append(float(file_lines[line_num+21][11: -1])) # max speed
    step_log.append(float(file_lines[line_num+22][17: -1])) # track direction
    step_log.append(float(file_lines[line_num+23][21: -1])) # steering difference
    step_log.append(float(file_lines[line_num+24][20: -1])) # heading difference
    step_log.append(float(file_lines[line_num+25][25: -1])) # distance from race line
    step_log.append(float(file_lines[line_num+26][16: -1])) # track_fraction
    step_log.append(float(file_lines[line_num+27][18: -1])) # speed difference
    step_log.append(float(file_lines[line_num+28][18: -1])) # lookahead_points
    step_log.append(file_lines[line_num+29][9: -1]) # penalty
    episode.append(copy.deepcopy(step_log))
    step_log = []
    line_num += 28

  line_num += 1


os.makedirs('%s/pickles/' % dir_name, exist_ok=True)

with open('%s/pickles/%s.pickle' % (dir_name, log_name[:-4]), 'wb') as f:
  pickle.dump(episodes, f)

