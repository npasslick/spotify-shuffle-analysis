'''
This script skips a number of songs on Spotify and writes corresponding hashes of the current song to a CSV file.
Please start the script with Spotify open and on 'PAUSE'!

@author: Nico Passlick
'''


from SwSpotify import spotify
import hashlib
import pyautogui
import sys
import time


# Functions for media keys
def play_pause():
    pyautogui.press('playpause')

def next_track():
    pyautogui.press('nexttrack')

def prev_track():
    pyautogui.press('prevtrack')


# Hash value calculation (SHA1)
def hash(value):
    hashObject = hashlib.sha1(value.encode())
    return hashObject.hexdigest()


# Loop over tracks and write hash to file
def write_tracks(qty):
    data = open('data.csv', 'a', newline='\n')
    play_pause()

    for i in range(qty):
        time.sleep(0.7)
        hashValue = hash('SONG=' + spotify.song() + ';' +
                         'ARTIST=' + spotify.artist())
        data.write(hashValue + '\n')
        print('Track {}/{}'.format(i+1, qty))
        next_track()

    play_pause()
    data.close()


if __name__ == "__main__":
    write_tracks(int(sys.argv[1]))
