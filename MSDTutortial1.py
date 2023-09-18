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
subset_data_path = r"C:\Users\aubre\Desktop\Capstone\Music-Genre-Classifier\Data"
#subset_data_path = r"C:\Users\aubre\Desktop\Capstone\Music-Genre-Classifier\Data\MillionSongSubset"
#subset_addf_path = os.path.join(subset_data_path, "AdditionalFiles")

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

""" Getting a Random List of 10 Artist Names """
# #measures how long it takes to get to get all artist names
# t1 = time.time()
# apply_to_all_files(subset_data_path, func = func_to_get_artist_name)
# t2 = time.time()

# #estimated average time it takes to print: 1:00 - 2:00
# print("all artist names extracted in: " + strtimedelta(t1, t2))
# #1st result -> 1:13:49 (minute, second, milisecond)

# print("found " + str(len(allArtistNames)) + " unique artist names")
# #expected result -> found 4412 unique artist names

# print("---\nlist of 10 artists")
# for k in range(10):
#     print(list(allArtistNames)[k].decode("utf-8"))
# print("---")

""" setting up SQLite or whatever (or trying to) """
conn = sqlite3.connect(os.path.join(subset_data_path, "subset_track_metadata.db"))

#build SQL query
q = "SELECT DISTINCT artist_name FROM songs"
#query the database
t1 = time.time()
res = conn.execute(q)
all_artist_names_sqlite = res.fetchall()
t2 = time.time()
print("all artist names extracted (SQLite) in: " + strtimedelta(t1, t2))

""" needs the SQLite thing???? """
# #count sounds for artists
# files_per_artist = {}
# for aid in all_artist_ids:
#     files_per_artist[aid] = 0

# def func_to_count_artist_id(filename):
#     h5 = GETTERS.open_h5_file_read(filename)
#     artist_id = GETTERS.get_artist_id(h5)
#     files_per_artist[artist_id] += 1
#     h5.close()

# apply_to_all_files(subset_data_path, func = func_to_count_artist_id)
# most_pop_aid = sorted(files_per_artist,
#                       key = files_per_artist.__getitem__,
#                       reverse = True)[0]
# print(most_pop_aid + " has " + files_per_artist[most_pop_aid] + " songs")