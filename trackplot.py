import numpy as np
import matplotlib.pyplot as plt

track_widths = {
    'fumiaki': 0.5
}

# Track Name from Tracks List
track_name = "fumiaki"
# Location of tracks folder
absolute_path = "."
# Get waypoints from numpy file
waypoints = np.load("%s/track_waypoints/%s.npy" % (absolute_path, track_name))
# Get number of waypoints
print("Number of waypoints = " + str(waypoints.shape[0]))
# Plot waypoints
for i, point in enumerate(waypoints):

    circle1 = plt.Circle((point[0], point[1]), track_widths['fumiaki'], color='r')
    ax = plt.gca()
    ax.add_patch(circle1)
    plt.scatter(point[0], point[1], c='blue')

plt.savefig('track.png')