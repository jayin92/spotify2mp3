import urllib.request
from bs4 import BeautifulSoup
import urllib
import youtube_dl
import os
import json
import requests
from termcolor import cprint
import re
# x = urllib.request.Request("https://www.youtubeto.com/zh/?v=1-xGerv5FOk")
# data = urllib.request.urlopen(x)
# print(data.read())


# import urllib2

error = []


def youtubeSearch(text):
    query = urllib.parse.urlencode({"search_query": text})
    url = "https://www.youtube.com/results?search_query=" + query
    print(url)
    response = urllib.request.urlopen(url)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', response.read().decode())
    url = "http://www.youtube.com/watch?v=" + search_results[0]
    return url
    # except:
    #     cprint("Can't find the song : {}".format(text), 'red')
    #     errorr = "error"
    #     error.append(text)
    #     return errorr


file = open("api.json", "r", encoding='UTF-8')
raw_text = file.read()
data = json.loads(raw_text)
file.close()

n = 0
songs = []
for track in data['items']:
    # print(track)
    if n == 0:
        artists = track['track']['artists'][0]['name']
    name = track['track']['name']
    song = str(artists + '-' + name)
    # song = song.replace(' ', '')
    songs.append(song)
    # print(track['track'['album'['name']]])

for song in songs:
    cprint("Current Song:{}".format(song), "green")
    url = youtubeSearch(song)
    if url is not "error":
        cmd = 'youtube-dl.exe --extract-audio --audio-format mp3 ' + url
        try:
            os.system(cmd)
        except:
            error.append(song)

print('ALL SONGS HAVE　BEEN DOWNLOADED')
print("Missing:")
for item in error:
    print(item)
