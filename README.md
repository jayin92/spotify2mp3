# spotify2mp3

這是一個能將Spotify歌單內的音樂下載下來並轉成 .mp3 的Python程式

## 安裝說明

請先確定電腦內已安裝 curl 及 beautifulsoup4

curl 安裝說明：https://www.cnblogs.com/xing901022/p/4652624.html

beautifulsoup4安裝： `pip install beautifulsoup4`

## 使用說明

以 STMPD RCRD TOP 50 這個歌單當作例子：
![image](https://i.imgur.com/Txy8DBj.png)
複製後的播放清單連結如下：
https://open.spotify.com/user/stmpdrcrds/playlist/1OIzwJTbrOeZTHvUXf5yMg?si=4WPrECM2R7ShKbNf0X1EzA

`user_id` 就是在user後面的 `stmpdrccds`

`playlist_id` 就是playlist到 ? 之間的 `1OIzwJTbrOeZTHvUXf5yMg`

![image](https://i.imgur.com/TMw93tc.png)
進入 https://developer.spotify.com/console/get-playlist-tracks，並將 user_id 及 playlist_id 填入欄位

填入點選綠色的 GET TOKEN 按鈕依照指示完成後

複製上圖反白的文字並加上` > api.json` 後，在clone的資料夾內執行
e.g.
`curl -X "GET" "https://api.spotify.com/v1/users/stmpdrccds/playlists/1OIzwJTbrOeZTHvUXf5yMg/tracks" -H "Accept: application/json" -H "Content-Type: application/json" -H "Authorization: Bearer BQARB8rLaVVRnW7ps5XKNpOZBs3bpgfa9un13rxWt2qqKuoihWEJKhVkSpe9a-MZTPc4GkamSmJE-QFZvS7tFdw9EoHmN2Qn4UjFI9DnASe6NbyZl0yD9WHwgfasZ2RMrFDZGQfWo0jNGJ11SdjKbhFmddVV86qFuc3C9_V9P869ES9Grd4Doje0oN8N84DXnvAFfbLsNmHLZPZOAslwfyGhHrrUYi0zFI4UZQw3x_5cbi6eZuzVuH8SUKB7CMDhYm6NqVNhwxXYdQ" > api.json
`

最後執行 `python mp3.py` 就可以開始下載
