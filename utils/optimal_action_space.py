import os
import sys
import math
import argparse
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

parser = argparse.ArgumentParser(description='A tool used to process waypoints obtained from a .npy file')
parser.add_argument('--track_name', type=str, nargs=1, help='REQUIRED - Name of the track, example: reinvent2018', required=True)
parser.add_argument('--look_ahead_points', dest='look_ahead_points', type=int, default=0, help='OPTIONAL - How far the algorithm look ahead to see when to brake. The higher the number, the earlier it will slow down. (default: 0)')
parser.add_argument('--min_speed', dest='min_speed', type=float, default=1, help='OPTIONAL - Minimum speed of the car (default: 1)')
parser.add_argument('--max_speed', dest='max_speed', type=float, default=4, help='OPTIONAL - Maximum speed of the car (default: 4)')


args = parser.parse_args()
track_name, look_ahead_points, min_speed, max_speed = args.track_name[0], args.look_ahead_points, args.min_speed, args.max_speed

# Get points from .npy files
dir_name = os.path.dirname(os.path.abspath(__file__))
race_line = np.load('%s/../tracks/optimal_track_points/%s.npy' % (dir_name, track_name))

# ------------------------ Calculation Functions ------------------------- #

# all functions taken directly from https://github.com/cdthompson/deepracer-k1999-race-lines/blob/master/Race-Line-Calculation.ipynb

# Uses previous and next coords to calculate the radius of the curve
# so you need to pass a list with form [[x1,y1],[x2,y2],[x3,y3]]
# Input 3 coords [[x1,y1],[x2,y2],[x3,y3]]
def circle_radius(coords):

    # Flatten the list and assign to variables (makes code easier to read later)
    x1, y1, x2, y2, x3, y3 = [i for sub in coords for i in sub]

    a = x1*(y2-y3) - y1*(x2-x3) + x2*y3 - x3*y2
    b = (x1**2+y1**2)*(y3-y2) + (x2**2+y2**2)*(y1-y3) + (x3**2+y3**2)*(y2-y1)
    c = (x1**2+y1**2)*(x2-x3) + (x2**2+y2**2)*(x3-x1) + (x3**2+y3**2)*(x1-x2)
    d = (x1**2+y1**2)*(x3*y2-x2*y3) + (x2**2+y2**2) * \
        (x1*y3-x3*y1) + (x3**2+y3**2)*(x2*y1-x1*y2)

    # In case a is zero (so radius is infinity)
    try:
        r = abs((b**2+c**2-4*a*d) / abs(4*a**2)) ** 0.5
    except:
        r = 999

    return r


# Returns indexes of next index and index+lookfront
# We need this to calculate the radius for next track section.
def circle_indexes(mylist, index_car, add_index_1=0, add_index_2=0):

    list_len = len(mylist)

    # if index >= list_len:
    #     raise ValueError("Index out of range in circle_indexes()")

    # Use modulo to consider that track is cyclical
    index_1 = (index_car + add_index_1) % list_len
    index_2 = (index_car + add_index_2) % list_len

    return [index_car, index_1, index_2]


def optimal_velocity(track, min_speed, max_speed, look_ahead_points):

  # Calculate the radius for every point of the track
  radius = []
  for i in range(len(track)):
    indexes = circle_indexes(track, i, add_index_1=-1, add_index_2=1)
    coords = [track[indexes[0]], track[indexes[1]], track[indexes[2]]]
    radius.append(circle_radius(coords))

  # Get the max_velocity for the smallest radius
  # That value should multiplied by a constant multiple
  v_min_r = min(radius)**0.5
  constant_multiple = min_speed / v_min_r
  print(f"Constant multiple for optimal speed: {constant_multiple}")

  if look_ahead_points == 0:
    # Get the maximal velocity from radius
    max_velocity = [(constant_multiple * i**0.5) for i in radius]
    # Get velocity from max_velocity (cap at MAX_SPEED)
    velocity = [min(v, max_speed) for v in max_velocity]
    return velocity

  else:
    # Looks at the next n radii of points and takes the minimum
    # goal: reduce lookahead until car crashes bc no time to break
    LOOK_AHEAD_POINTS = look_ahead_points
    radius_lookahead = []
    for i in range(len(radius)):
      next_n_radius = []
      for j in range(LOOK_AHEAD_POINTS+1):
        index = circle_indexes(mylist=radius, index_car=i, add_index_1=j)[1]
        next_n_radius.append(radius[index])
      radius_lookahead.append(min(next_n_radius))
    max_velocity_lookahead = [(constant_multiple * i**0.5) for i in radius_lookahead]
    velocity_lookahead = [min(v, max_speed) for v in max_velocity_lookahead]
    return velocity_lookahead


# For each point in racing track, check if left curve (returns boolean)
def is_left_curve(coords):

  # Flatten the list and assign to variables (makes code easier to read later)
  x1, y1, x2, y2, x3, y3 = [i for sub in coords for i in sub]

  return ((x2-x1)*(y3-y1) - (y2-y1)*(x3-x1)) > 0


# Calculate the distance between 2 points
def dist_2_points(x1, x2, y1, y2):
        return abs(abs(x1-x2)**2 + abs(y1-y2)**2)**0.5


# ------------------------ Optimal Speed Calculation and Visualization ------------------------- #

# all functions taken directly from https://github.com/cdthompson/deepracer-k1999-race-lines/blob/master/Race-Line-Calculation.ipynb

velocities = optimal_velocity(race_line, min_speed, max_speed, look_ahead_points)
distance_to_prev = []
for i in range(len(race_line)):
    indexes = circle_indexes(race_line, i, add_index_1=-1, add_index_2=0)[0:2]
    coords = [race_line[indexes[0]], race_line[indexes[1]]]
    dist_to_prev = dist_2_points(x1=coords[0][0], x2=coords[1][0], y1=coords[0][1], y2=coords[1][1])
    distance_to_prev.append(dist_to_prev)
    
time_to_prev = [(distance_to_prev[i]/velocities[i]) for i in range(len(race_line))]

total_time = sum(time_to_prev)
print(f"Total time for track, if racing line and speeds are followed perfectly: {total_time} s")

fig, ax = plt.subplots()
ax = sns.scatterplot(x=[i[0] for i in race_line], y=[i[1] for i in race_line], hue=velocities, palette="vlag").set_title("Optimal Velocity Heatmap")
os.makedirs('%s/plots/speed_maps' % os.path.abspath(os.path.join(dir_name, '..')), exist_ok=True)
plt.savefig('%s/../plots/speed_maps/%s.png' % (dir_name, track_name))
print('Image saved as plots/speed_maps/%s.png' % track_name)


# ------------------------ Optimal Action Space Calculation and Visualization ------------------------- #

radius = []
for i in range(len(race_line)):
  indexes = circle_indexes(race_line, i, add_index_1=-1, add_index_2=1) # CHANGE BACK? 1;2
  coords = [race_line[indexes[0]], race_line[indexes[1]], race_line[indexes[2]]]
  radius.append(circle_radius(coords))

# Calculate curve direction
left_curve = []
for i in range(len(race_line)):
  indexes = circle_indexes(race_line, i, add_index_1=-1, add_index_2=1)
  coords = [race_line[indexes[1]], race_line[indexes[0]], race_line[indexes[2]]]
  left_curve.append(is_left_curve(coords))

# Calculate radius with + and - for direction (+ is left, - is right)
radius_direction = []
for i in range(len(race_line)):
  radius_with_direction = radius[i]
  if left_curve[i] == False:
    radius_with_direction *= -1
  radius_direction.append(radius_with_direction)

# Calculate steering with + and -
dist_wheels_front_back = 0.165 # meters
steering = []
for i in range(len(race_line)):
  steer = math.degrees(math.asin(dist_wheels_front_back/radius_direction[i]))
  steering.append(steer)

velocities = np.array(velocities)
steering = np.array(steering)

path = os.path.abspath(os.path.join(dir_name, '..', 'action_space'))
os.makedirs('%s/velocities' % path, exist_ok=True)
os.makedirs('%s/steering_angles' % path, exist_ok=True)

np.save(os.path.join(path, 'velocities', '%s.npy' % track_name), velocities)
print('Saved optimal velocities for %s track under %s' % (track_name, os.path.relpath(path)))
np.save(os.path.join(path, 'steering_angles', '%s.npy' % track_name), steering)
print('Saved optimal steering angles for %s track under %s' % (track_name, os.path.relpath(path)))

fig, ax = plt.subplots()
ax = sns.scatterplot(data={'velocity': velocities, 'steering': steering }, x="steering", y="velocity")
ax.set_title(f"With lookahead: {look_ahead_points}")
os.makedirs('%s/plots/action_space' % os.path.abspath(os.path.join(dir_name, '..')), exist_ok=True)
plt.savefig('%s/../plots/action_space/%s.png' % (dir_name, track_name))
print('Image saved as plots/action_space/%s.png' % track_name)
