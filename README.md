# DeepRacer


## Getting Started

First ensure that you have [python3 with pip (a package manager for python) installed](https://www.python.org/downloads/).

```
pip install argparse numpy matplotlib
```

If you are working on windows, I strongly recommend installing   [7-zip](https://www.7-zip.org/) to help unzip files extracted from the deepracer simulation logs.

Now we get to the fun stuff.

## Tracks

Inside the `tracks/` directory you will find a `tracks.json` file.

This file contains arrays of waypoints and the track widths for several tracks. The file already contains some sample data (though you should grab this track data yourself from the sim logs as you won't know if these values change from year to year).

`tracks.json` acts as the single source of truth for track information in this project, so modifications here will cascade down with the help of `utils/process_tracks.py`.

## Utils

### process_tracks.py

This file is responsible for parsing and saving the data stored in `tracks.json`. Run the following:

```
python utils/process_tracks.py
```

and you will see some new directories created under the `tracks/` directory. These directories contain numpy arrays of waypoints of each of the tracks, as well as the computed boundaries of the tracks. These are what every other file in this project will be using for analysis / further processing.

Whenever you make changes to `tracks/tracks.json`, ensure that you run the `utils/process_tracks.py` script in order for those changes to be accurately represented.

### plot_track.py

This is a tool to plot a graph of any of the tracks you have saved and processed. To get started, try running:
```bash
python utils/plot_track.py --track_name reinvent2018
```
You should see a new directory called `plots/` with a scatterplot image of the reInvent 2018 track inside.

For a full list of arguments, run:
```
python utils/plot_track.py --help
```
