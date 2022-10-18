import os

dir_name = os.path.dirname(os.path.abspath(__file__))
path = os.path.abspath(os.path.join(dir_name, 'log.txt'))

file = open(path, 'r')
reward = 0
progress = 0
started = False
finished = False
for line in file:
  if ('## agent: Starting evaluation phase' in line):
    started = True
    finished = False
  if ('## agent: Finished evaluation phase.' in line):
    started = False
    finished = True
    print(reward)
    reward = 0
  if ('REWARDS:' in line and started):
    trl = line.find('total_reward')
    tr = line[trl+13:-2]
    tr = float(tr)
    reward += tr