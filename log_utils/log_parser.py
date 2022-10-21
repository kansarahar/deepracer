import os
import sys
import copy
import pickle

log_name = 'ace-training-2.log'
dir_name = os.path.dirname(os.path.abspath(__file__))
path = os.path.abspath(os.path.join(dir_name, log_name))

file = open(path, 'r')
file_lines = file.readlines()
episodes = []
episode = []
rewards = [] # [steering, heading, center, speed, progress]

line_num = 0
while line_num < len(file_lines):
  line = file_lines[line_num]
  if (line == 'Reset agent finished\n' or line_num == len(file_lines)-1):
    if (episode): episodes.append(copy.deepcopy(episode))
    episode = []
  if (line == '=============== <REWARDS> ===============\n'):
    rewards.append(float(file_lines[line_num+1][17: -1])) # steering reward
    rewards.append(float(file_lines[line_num+2][16: -1])) # heading reward
    rewards.append(float(file_lines[line_num+3][15: -1])) # center reward
    rewards.append(float(file_lines[line_num+4][14: -1])) # speed reward
    rewards.append(float(file_lines[line_num+16][10: -1])) # progress
    episode.append(copy.deepcopy(rewards))
    rewards = []
    line_num += 16

  line_num += 1


os.makedirs('%s/pickles/' % dir_name, exist_ok=True)

with open('%s/pickles/%s.pickle' % (dir_name, log_name[:-4]), 'wb') as f:
  pickle.dump(episodes, f)

