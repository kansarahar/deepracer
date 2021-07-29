import numpy as np
import matplotlib.pyplot as plt
from numpy.core.defchararray import array

track_widths = np.load('track_widths.npy', allow_pickle=True).item()

# Track Name from Tracks List
track_name = "cumulo"
track_width = track_widths[track_name]

# Get waypoints from numpy file
[waypoints, innerpoints, outerpoints] = [np.load("./track_%s/%s.npy" % (points_set, track_name)) for points_set in ['waypoints', 'innerpoints', 'outerpoints']]
[waypoints, innerpoints, outerpoints] = [np.array(waypoints), np.array(innerpoints), np.array(outerpoints)]
print("Number of waypoints = " + str(waypoints.shape[0]))

# Plot waypoints as scatter
for i in range(len(waypoints)):
    waypoint, innerpoint, outerpoint = waypoints[i], innerpoints[i], outerpoints[i]
    # Label every 10 points with a number on the plot
    # if (i % 10 == 0):
    #     plt.text(waypoint[0] * (1 + 0.01), waypoint[1] * (1 + 0.01) , i, fontsize=10)
    plt.scatter(waypoint[0], waypoint[1], c='blue')
    plt.scatter(innerpoint[0], innerpoint[1], c='red')
    plt.scatter(outerpoint[0], outerpoint[1], c='green')

# Plot waypoints as lines
# [plt.plot([point[0] for point in points], [point[1] for point in points]) for points in [innerpoints, waypoints, outerpoints]]

img_name = 'track.png'
plt.savefig(img_name)
print('image saved as %s' % img_name)