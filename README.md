# What is this

This is a small script to plot a gpx route on a map, along with the relative timestamps.

# Background story

When editing my ski and other sports videos, I use Virb Edit (a now abandonned video editing tool from Garmin) to overlay informations from my Garmin watch onto the video (for instance: elevation, speed, etc). This requires to sync the video and the track from the watch, which used to be possible to do in Virb Edit using a map that showed the activity trace. Unfortunately, this functionality broke. So I wrote this script to plot the track onto a map, along with the timestamps. That way I can keep syncing the video and track from the watch.

# Usage

This is what I do, working as of 2025-01-06:

* export the .fit file from the Garmin, using a Mac app called "Android File Transfer"
* convert the .fit file into a .gpx track file, using the converter tool of the "AllTrails" website
* install the packages from `requirements.txt` into a Python virtual environment
* run the script with `python gpx_map_plotter.py --filename <path to the gpx>`
* open the file `map.html` that has been created
* find a point of my video with a visual landmark (e.g. sharp turn)
* find the same point in the map, and take a note of the timestamp by hovering over a marker
* use this in Virb Edit to do the sync

And voilà.

The file `example_map.png` shows an example of the generated map.
