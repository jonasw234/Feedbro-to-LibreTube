#!/usr/bin/env python3
"""Converts Feedbro YouTube subscriptions to LibrePipe subscriptions."""
import json
import sys
import xml.etree.ElementTree as ET
from os.path import basename


def main(feedbro_input: str, libretube_output: str):
    """Convert Feedbro YouTube subscriptions to LibreTube subscriptions.

    Parameters
    ----------
    feedbro_input : str
        Feedbro input file
    libretube_output : str
        LibreTube output file
    """
    # Parse Feedbro opml export
    feedbro_tree = ET.parse(feedbro_input)
    prefix = "https://www.youtube.com/channel/"
    youtube_channels = [
        {"channelId": channel.attrib["htmlUrl"][len(prefix) :]}
        for channel in feedbro_tree.iter()
        if channel.attrib.get("htmlUrl")
        and channel.attrib["htmlUrl"].startswith(prefix)
    ]

    # Export to LibreTube database file
    libretube = None
    with open(libretube_output, "r") as libretube_file:
        libretube = json.load(libretube_file)
    libretube["localSubscriptions"] = youtube_channels
    with open(libretube_output, "w") as libretube_file:
        json.dump(libretube, libretube_file)

    print(f"Export completed and saved to {libretube_output}.")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {basename(__file__)} Feedbro-Subscriptions.opml LibreTube.json")
        sys.exit(1)
    else:
        main(*sys.argv[1:])
