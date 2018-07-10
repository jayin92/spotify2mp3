import urllib.request
from bs4 import BeautifulSoup
import urllib
import os
import json
import requests
from termcolor import cprint
import re
from pyfiglet import figlet_format


def youtubeSearch(text):
    query = urllib.parse.urlencode({"search_query": text})
    url = "https://www.youtube.com/results?search_query=" + query
    print(url)
    response = urllib.request.urlopen(url)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', response.read().decode())
    url = "http://www.youtube.com/watch?v=" + search_results[0]
    return url


error = []
cprint(figlet_format('spotify 2 mp3'), 'cyan')

playlist_url = str(input("請輸入播放清單分享網址："))
split_url = playlist_url.split("/")
user_id = split_url[4]
playlist_id = split_url[6]
print("  ")
cprint("oauth token 獲取網址 : https://developer.spotify.com/console/get-playlist/", "cyan")
print("  ")
oauth_token = str(input("請輸入token："))

curl_cmd = (('curl -X "GET" "https://api.spotify.com/v1/users/{}/playlists/{}/tracks"'
            ' -H "Accept: application/json" -H "Content-Type: application/json"'
            ' -H "Authorization: Bearer {}" > api.json').format(user_id, playlist_id, oauth_token))

print("取得歌曲中...")
# print(curl_cmd)
os.system(curl_cmd)

file = open("api.json", "r", encoding='UTF-8')
raw_text = file.read()
data = json.loads(raw_text)
file.close()

n = 0
songs = []
try:
    for track in data['tracks']['items']:
        print(track)
        if n == 0:
            artists = track['track']['artists'][0]['name']
        name = track['track']['name']
        song = str(artists + '-' + name)
        songs.append(song)
    print("此播放清單共有{}首歌".format(len(songs)))
except:
    cprint("此token已過期，請到 https://developer.spotify.com/console/get-playlist-tracks 來重新認證", "red")


else:
    for song in songs:
        cprint("下載歌曲:{}".format(song), "green")
        try:
            url = youtubeSearch(song)
        except:
            error.append(song)
            print('找不到{}'.format(song))
        else:
            if url is not "error":
                cmd = 'youtube-dl.exe --extract-audio --audio-format mp3 --audio-quality 0 ' + url
                try:
                    os.system(cmd)
                except:
                    error.append(song)

    cprint("歌曲下載完畢", "green")
    print("未成功下載：")
    for item in error:
        print(item)
