'''
This script skips a number of songs on Spotify and writes corresponding hashes of the current song to a CSV file.
Please start the script with Spotify open and on 'PAUSE'!

@author: Nico Passlick
'''


from SwSpotify import spotify
import hashlib
import pyautogui
import time


def playPause():
    pyautogui.press('playpause')

def nextTrack():
    pyautogui.press('nexttrack')

def prevTrack():
    pyautogui.press('prevtrack')


def hash(value):
    hashObject = hashlib.sha1(value.encode())
    return hashObject.hexdigest()


def writeTracks(qty):
    data = open('data.csv', 'a', newline='\n')
    playPause()

    for i in range(qty):
        hashValue = hash('SONG=' + spotify.song() + ';' +
                         'ARTIST=' + spotify.artist())
        data.write(hashValue + '\n')
        time.sleep(0.5)
        nextTrack()

    playPause()
    data.close()


if __name__ == "__main__":
    writeTracks(50)
