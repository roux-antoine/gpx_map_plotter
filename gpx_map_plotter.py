import matplotlib.pyplot as plt
from xml.dom import minidom
import utm
from datetime import datetime

import folium
import argparse

"""
See the readme
"""


def plot_gpx_map(filename: str, plot_matplotlib: bool, plot_folium: bool, subsample_step: int):
    # Read GPX file
    data = open(filename)
    xmldoc = minidom.parse(data)
    tracks = xmldoc.getElementsByTagName("trkpt")
    times = xmldoc.getElementsByTagName("time")

    # parse elements
    lon_list = [float(track.attributes["lon"].value) for track in tracks]
    lat_list = [float(track.attributes["lat"].value) for track in tracks]
    times = [
        datetime.strptime(t.firstChild.nodeValue, "%Y-%m-%dT%H:%M:%SZ") for t in times[1:]
    ]  # skipping first one because it corresponds to file creation time

    relative_times = [t - times[0] for t in times]

    if plot_matplotlib:
        for lat, lon, relative_t in zip(
            lat_list[::subsample_step], lon_list[::subsample_step], relative_times[::subsample_step]
        ):
            utm_values = utm.from_latlon(lat, lon)
            x_utm, y_utm = utm_values[0], utm_values[1]
            plt.scatter(x_utm, y_utm, color="green", label=relative_t)

        plt.legend()
        plt.show()
    else:
        print("Skipping plotting with matplotlib")

    # Create the map
    if plot_folium:
        my_map = folium.Map(location=[lat_list[0], lon_list[0]], zoom_start=15)
        for lat, lon, relative_t in zip(
            lat_list[::subsample_step], lon_list[::subsample_step], relative_times[::subsample_step]
        ):

            # Add markers to the map
            folium.Marker([lat, lon], popup=relative_t).add_to(my_map)

        # Display the map
        map_filename = "map.html"
        my_map.save(map_filename)
        print(f"Saved the map to {map_filename}")
    else:
        print("Skipping plotting with folium")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # Add arguments
    parser.add_argument(
        "--filename",
        help="Path to gpx track file",
        default=False,
        required=True,
    )
    parser.add_argument(
        "--plot-matplotlib",
        action="store_true",
        help="Enable plotting using Matplotlib.",
        default=False,
    )
    parser.add_argument(
        "--plot-folium",
        action="store_true",
        help="Enable plotting using Folium.",
        default=True,
    )
    parser.add_argument(
        "--subsample-step",
        type=int,
        default=4,
        help="How many steps to jump when subsampling",
    )

    # Parse the arguments
    args = parser.parse_args()

    plot_gpx_map(
        filename=args.filename,
        plot_matplotlib=args.plot_matplotlib,
        plot_folium=args.plot_folium,
        subsample_step=args.subsample_step,
    )
