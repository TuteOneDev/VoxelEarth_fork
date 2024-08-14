# This is a simple interface for automate the most posible
# the installation and execution of every VoxelEarth's script

import os
import tkinter as tk
from tkinter import filedialog

tiles_dl_master_path = "../3dtiles-dl-master/"

def select_folder():
    root = tk.Tk()
    root.withdraw()

    folder = filedialog.askdirectory()

    return folder

# ToDo: Add options for voxelize with CPU or GPU method and automate another process
menu = """
╔════════════════════════════════╗
║ https://voxelearth.org         ║
╠════════════════════════════════╣
║ Choose an option:              ║
║ 0. Install python requirements ║
║ 1. Tiles downloader            ║
║ 2. Tiles combiner              ║
║ 3. Exit                        ║
╚════════════════════════════════╝
_> """

while True:
    try:
        os.system("cls")

        i_menu = int(input(menu))

        os.system("cls")
        match i_menu:
            case 0:
                print("Installing dependencies: numpy, tqdm, bpy, requests, pillow\n")
                os.system("pip install numpy tqdm bpy requests pillow")

            case 1:
                # ToDo: Add system for save and load the API key from file using a function
                apiKey = input("Enter your Google API key: ")
                coords = input("Enter the coordinates (longitude latitude): ")
                radius = input("Enter the radius: ")
                outputDir = select_folder()

                # Go to 3dtiles_dl_master folder and execute the downloader script with arguments:
                # GoogleMaps API key, Coords (longitude-latitude), radius and outputDirectory
                os.system(
                    f"cd {tiles_dl_master_path} && python -m threaded_api -k {apiKey} -c {coords} -r {radius} -o {outputDir}"
                )

            case 2:
                # ToDo: Add more information for the user
                originDir = select_folder()
                outputDir = select_folder()

                # Go to 3dtiles_dl_master folder and execute the combiner script with the arguments:
                # origin directory and output directory for combine GLB files
                os.system(
                    f"cd {tiles_dl_master_path} && python.exe combine_glb.py -- {originDir}/ {outputDir}/combined.glb"
                )

            case 3:
                break

        os.system("pause")

    # ToDo: Add specific exceptions
    except:
        pass
