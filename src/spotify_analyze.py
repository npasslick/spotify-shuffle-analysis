'''
This script provides data analysis tools for the gathered data by the Spotify shuffle runs.

@author: Nico Passlick
'''


from collections import defaultdict
import csv
import sys


# Counts duplicate tracks in CSV file
def count_tracks(path_in, path_out):
    file_in = open(path_in, 'r', newline='\n')
    file_out = open(path_out, 'w', newline='\n')
    data = csv.reader(file_in)
    count = csv.writer(file_out)
    tracks = defaultdict(int)

    for row in data:
        tracks[row[0]] += 1

    for row in tracks.items():
        count.writerow(row)


if __name__ == "__main__":
    if (len(sys.argv) > 1 and sys.argv[1] == 'count'):
        count_tracks(sys.argv[2], sys.argv[3])
    else:
        print('Please provide args for method!')
