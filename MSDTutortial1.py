"""
Music Genre Classifier
Aubrey McGarrah

MSD Tutorial 1
    Following the Million Song Database Tutorial 1 (http://millionsongdataset.com/pages/tutorial/)
"""

import os
import sys
import time
import glob
import datetime
import sqlite3
import numpy as np

import hdf5_getters as GETTERS

#path to Million Song Dataset Subset
subset_data_path = r"C:\Users\aubre\Desktop\Capstone\Music-Genre-Classifier\Data\MillionSongSubset"

#time lag in seconds
def strtimedelta(startTime, stopTime):
    return str(datetime.timedelta(seconds = stopTime - startTime))

#iterate files
def apply_to_all_files(basedir, func = lambda x: x, ext = ".h5"):
    count = 0

    for root, dirs, files in os.walk(basedir):
        files = glob.glob(os.path.join(root, "*" + ext))
        count += len(files)

        for f in files:
            func(f)

    return count

print("number of song files: " + str(apply_to_all_files(subset_data_path)))
#expected result -> number of song files: 10000

allArtistNames = set()
def func_to_get_artist_name(fileName):
    h5 = GETTERS.open_h5_file_read(fileName)
    artistName = GETTERS.get_artist_name(h5)
    allArtistNames.add(artistName)
    h5.close()

#measures how long it takes to get to get all artist names
t1 = time.time()
apply_to_all_files(subset_data_path, func = func_to_get_artist_name)
t2 = time.time()

#estimated average time it takes to print: 1:00 - 2:00
print("all artist names extracted in: " + strtimedelta(t1, t2))
#1st result -> 1:13:49 (minute, second, milisecond)

print("found " + str(len(allArtistNames)) + " unique artist names")
#expected result -> found 4412 unique artist names

print("---\nlist of 10 artists")
for k in range(10):
    print(list(allArtistNames)[k].decode("utf-8"))
print("---")
