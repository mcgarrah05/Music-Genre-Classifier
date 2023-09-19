"""
Music Genre Classifier
Aubrey McGarrah

Data Collection
    Getting data from the song files in the Million Song Database using the GETTERS functions

    Factors I'm Looking At:
        - song name
        - artist name
        - artist location
        - danceability
        - energy
        - key / key confidence
        - loudness
        - tempo
        - time signature / time sig. confidence
        - year
        - genre (self-classifying)
"""

import os
import datetime
import glob

import hdf5_getters as GETTERS

#path to MSD subset
subset_data_path = r"C:\Users\aubre\Desktop\Capstone\Music-Genre-Classifier\Data"

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

# #print number of song files (10000)
# print("number of song files: " + str(apply_to_all_files(subset_data_path)))

#gets data from song file
def collect_data(songFile):
    song = GETTERS.open_h5_file_read(songFile)

    #song/artist information
    songTitle = GETTERS.get_title(song)
    artistName = GETTERS.get_artist_name(song)
    artistLocation = GETTERS.get_artist_location(song)

    #song parameters
    danceability = GETTERS.get_danceability(song)
    energy = GETTERS.get_energy(song)
    key = GETTERS.get_key(song)
    keyConfidence = GETTERS.get_key_confidence(song)
    loudness = GETTERS.get_loudness(song)
    tempo = GETTERS.get_tempo(song)
    timeSignature = GETTERS.get_time_signature(song)
    timeSigConfidence = GETTERS.get_time_signature_confidence(song)
    year = GETTERS.get_year(song)

    #data dictionary
    data = {
        #song/artist information
        "song name": songTitle,
        "artist": artistName,
        "artist location": artistLocation,

        #song parameters
        "danceability": danceability,
        "energy": energy,
        "key": key,
        "key confidence": keyConfidence,
        "loudness": loudness,
        "tempo": tempo,
        "time signature": timeSignature,
        "time sig. confidence": timeSigConfidence,
        "year": year,
        "genre": ""
    }