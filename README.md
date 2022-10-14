# DeepRacer


## Getting Started

First ensure that you have [python3 with pip (a package manager for python) installed](https://www.python.org/downloads/).

```
pip install argparse numpy matplotlib shapely seaborn
```

If you are working on windows, I strongly recommend installing   [7-zip](https://www.7-zip.org/) to help unzip files extracted from the deepracer simulation logs.

Now we get to the fun stuff.


## Utils

### track_data.py

Inside the `utils/` directory you will find a `track_data.py` file.

This file contains arrays of waypoints and the track widths for several tracks. The file already contains some sample data (though you should grab this track data yourself from the sim logs as you won't know if these values change from year to year).

`track_data.py` acts as the single source of truth for track information in this project, so modifications here will cascade down with the help of `utils/process_tracks.py`.

### process_tracks.py

This file is responsible for parsing and saving the data stored in `track_data.py`. Run the following:

```
python utils/process_tracks.py
```

and you will see some new .npy files created under the new `tracks/track_points` directory. These files contain numpy arrays of waypoints of each of the tracks, as well as the computed boundaries of the tracks. These are what every other file in this project will be using for analysis / further processing.

Whenever you make changes to `utils/track_data.py`, ensure that you run the `utils/process_tracks.py` script in order for those changes to be accurately represented.

### plot_track.py

This is a tool to plot a graph of any of the tracks you have saved and processed. To get started, try running:
```bash
python utils/plot_track.py --track_name reinvent2018
```
You should see a new directory called `plots/tracks` with a scatterplot image of the reInvent 2018 track inside.

For a full list of arguments, run:
```
python utils/plot_track.py --help
```

### optimal_path.py

This is a tool to create, save, and plot the optimal path around the track via the k1999 algorithm. Don't worry, you don't need to know the details of the algorithm to run this script. Once you have processed the tracks via `utils/process_tracks.py`, you can try running:
```bash
python utils/optimal_path.py --track_name reinvent2018
```
After some time, you should see a new image under `plots/optimal_paths/reinvent2018.png` with a scatterplot image of the reInvent 2018 track inside. You should also see a `tracks/optimal_track_points/reinvent2018.npy` file as well. You can later load this file into a numpy array, print it, and copy/paste it into your reward function to use however you see fit.

For a full list of arguments, run:
```
python utils/optimal_path.py --help
```

### optimal_action_space.py

This is a tool to create and visualize the speed and steering angles around the optimal path created in the previous step. Again, the details of this algorithm aren't critical to knowing how to use this script. Try running:
```bash
python utils/optimal_action_space.py --track_name reinvent2018
```

This will create two plots: one under `plots/speed_maps/` and one under `plots/action_space/`. The first describes the optimal speed at each point along the calculated optimal racing line. The second is a scatter plot of the calculated steering angles vs the calculated speeds. Use this scatterplot to determine your action space.

This also creates two .npy files under the new `action_space/steering_angles` and `action_space/velocities` directories, and they just contain the calculated optimal speed and steering angles as numpy arrays. These can be used for further analysis if desired.

For a full list of arguments, run:
```
python utils/optimal_action_space.py --help
```

### clean.py

Used for cleaning up tracks, plots, and action_space directories