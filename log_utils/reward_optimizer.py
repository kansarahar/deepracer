import os
import pickle
import numpy as np
from sklearn.linear_model import LinearRegression

dir_name = os.path.dirname(os.path.abspath(__file__))

def loadData(pickled_file_name):
  file = open('%s/pickles/%s' % (dir_name, pickled_file_name), 'rb')
  episodes = pickle.load(file)
  file.close()
  return episodes

jochem_training_1_data = loadData('jochem-training-1.pickle')
ace_training_2_data = loadData('ace-training-2.pickle')
jochem_training_3_data = loadData('jochem-training-3.pickle')

##################### Basic Linear Model #####################
# a + b * steering_reward + c * heading_reward + d * center_reward + e * speed_reward ~= progress

def linearModelCoefficients(episodes):
  y = []
  x = []
  
  for episode in episodes:
    progress = episode[-1][-1]
    rewards = np.zeros(5)
    for step in episode:
      steering_reward = step[0] if step[0] > 0.1 else 0.1
      heading_reward = step[1] if step[1] > 0.1 else 0.1
      center_reward = step[2] if step[2] > 0.1 else 0.1
      speed_reward = step[3] if step[3] > 0.1 else 0.1
      rewards[0] += 1
      rewards[1] += steering_reward
      rewards[2] += heading_reward
      rewards[3] += center_reward
      rewards[4] += speed_reward
    y.append(progress)
    x.append(rewards)

  y = np.array(y)
  x = np.array(x)

  coeffs = LinearRegression(positive=True).fit(x, y).coef_
  return coeffs

# print(linearModelCoefficients(jochem_training_1_data))
# print(linearModelCoefficients(ace_training_2_data))
# print(linearModelCoefficients(jochem_training_3_data))
# print(linearModelCoefficients(jochem_training_1_data + ace_training_2_data + jochem_training_3_data))

##################### Basic Geometric Model #####################
# a + b * (steering_reward * heading_reward * center_reward * speed_reward) ~= progress

def geometricModelCoefficients(episodes):
  y = []
  x = []
  
  for episode in episodes:
    progress = episode[-1][-1]
    rewards = np.zeros(2) 
    for step in episode:
      steering_reward = step[0] if step[0] > 0.1 else 0.1
      heading_reward = step[1] if step[1] > 0.1 else 0.1
      center_reward = step[2] if step[2] > 0.1 else 0.1
      speed_reward = step[3] if step[3] > 0.1 else 0.1
      rewards[0] += 1
      rewards[1] += steering_reward *heading_reward * center_reward * speed_reward
    y.append(progress)
    x.append(rewards)

  y = np.array(y)
  x = np.array(x)


  coeffs = LinearRegression(positive=True).fit(x, y).coef_
  return coeffs

print(geometricModelCoefficients(jochem_training_1_data))
print(geometricModelCoefficients(ace_training_2_data))
print(geometricModelCoefficients(jochem_training_3_data))
print(geometricModelCoefficients(jochem_training_1_data + ace_training_2_data + jochem_training_3_data))



##################### Hybrid Model #####################
# x0 
# + x1*steering_reward + x2*heading_reward + x3*center_reward + x4*speed_reward 
# + x5*(steering_reward*heading_reward) + x6*(steering_reward*center_reward) + x7*(steering_reward*speed_reward)
# + x8*(heading_reward*center_reward) + x9*(heading_reward*speed_reward) + x10*(center_reward*speed_reward)
# + x11*(steering_reward*heading_reward*center_reward*speed_reward) 
# ~= progress

def linearModelCoefficients(episodes):
  y = []
  x = []
  
  for episode in episodes:
    progress = episode[-1][-1]
    rewards = np.zeros(12)
    for step in episode:
      steering_reward = step[0] if step[0] > 0.1 else 0.1
      heading_reward = step[1] if step[1] > 0.1 else 0.1
      center_reward = step[2] if step[2] > 0.1 else 0.1
      speed_reward = step[3] if step[3] > 0.1 else 0.1
      rewards[0] += 1
      rewards[1] += steering_reward
      rewards[2] += heading_reward
      rewards[3] += center_reward
      rewards[4] += speed_reward
      rewards[5] += steering_reward * heading_reward
      rewards[6] += steering_reward * center_reward
      rewards[7] += steering_reward * speed_reward
      rewards[8] += heading_reward * center_reward
      rewards[9] += heading_reward * speed_reward
      rewards[10] += center_reward * speed_reward
      rewards[11] += steering_reward * heading_reward * center_reward * speed_reward
    y.append(progress)
    x.append(rewards)

  y = np.array(y)
  x = np.array(x)


  coeffs = LinearRegression(positive=True).fit(x, y).coef_
  return coeffs

# print(hybridModelCoefficients(jochem_training_1_data))
# print(hybridModelCoefficients(ace_training_2_data))
# print(hybridModelCoefficients(jochem_training_3_data))
# print(hybridModelCoefficients(jochem_training_1_data + ace_training_2_data))
# print(hybridModelCoefficients(jochem_training_3_data + ace_training_2_data))

# [const      steer      head       center     spd          steer*head          steer*cent steer*spd  head*cent  head*spd   cent*spd   all       ]
# [0.20299424 0.03109448 0.01796492 0.00291123 0.           0.                  0.         0.19849211 0.         0.         0.         0.        ]
# [0.12171693 0.09676324 0.         0.         0.           0.                  0.         0.24701807 0.         0.         0.         0.        ]
# [0.19359417 0.         0.04777292 0.         0.17424407   0.00405046          0.         0.         0.01872545 0.10130339 0.         0.        ]
# [0.01608984 0.20224869 0.         0.02054101 0.33402001   0.                  0.         0.         0.         0.         0.         0.        ]
# [0.11966181 0.         0.         0.         0.58659928   0.                  0.         0.         0.         0.         0.         0.        ]