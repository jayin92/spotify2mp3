# spotify2mp3

這是一個能將Spotify歌單內的音樂下載下來並轉成 .mp3 的Python程式

## 安裝說明

請先確定電腦內已安裝 curl 及 beautifulsoup4

curl 安裝說明：https://www.cnblogs.com/xing901022/p/4652624.html

beautifulsoup4安裝： `pip install beautifulsoup4`

## 使用說明
執行 `python spotify2mp3.py` 
以 STMPD RCRD TOP 50 這個歌單當作例子：
![image](https://i.imgur.com/Txy8DBj.png)
複製後的播放清單連結如下：

https://open.spotify.com/user/stmpdrcrds/playlist/1OIzwJTbrOeZTHvUXf5yMg?si=4WPrECM2R7ShKbNf0X1EzA

將其貼入程式

進入 https://developer.spotify.com/console/get-playlist-tracks

並將綠色的 GET TOKEN 欄位複製後

在程式內貼上

即可開始下載

