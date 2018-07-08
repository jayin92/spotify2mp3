import json
import requests

playlist_url = "https://api.spotify.com/v1/users/11166905215/playlists/2DROwRlBKZuHUiAf2gmGu5/tracks"

file = open("api.txt",  encoding='UTF-8')
raw_text = file.read()
data = json.loads(raw_text)
n = 0
songs = []
for track in data['items']:
    # print(track)
    if n == 0:
        artists = track['track']['artists'][0]['name']
    name = track['track']['name']
    song = artists + '-' + name
    songs.append(song)
    # print(track['track'['album'['name']]])
