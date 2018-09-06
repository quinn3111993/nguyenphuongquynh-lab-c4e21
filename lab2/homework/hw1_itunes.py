# Part 1 - Crawl list from iTunes
from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import OrderedDict

url = 'https://www.apple.com/itunes/charts/songs'
conn = urlopen(url)

raw_data = conn.read()
html_page = raw_data.decode('utf-8')

soup = BeautifulSoup(html_page, 'html.parser')
div_list = soup.find_all('div', 'section-content')
li_list = div_list[1].ul.find_all('li')

song_list = []

for li in li_list:
    a = li.h3.a
    title = li.h3.a.string
    artist = li.h4.a.string
    link = li.h3.a['href']
    song = OrderedDict({
        'Title': title,
        'Artist': artist,
        'Link': link,
    })
    song_list.append(song)

import pyexcel
pyexcel.save_as(records=song_list, dest_file_name='Top_Songs.xlsx')


# Part 2 - Download from Youtube
from youtube_dl import YoutubeDL
dl = YoutubeDL()

options = {
    'default_search': 'ytsearch',
    'max_download': 1,
}

dl = YoutubeDL(options)
list_song = []
for song in song_list:
    song = song['Artist'] + ' ' + song['Title']
    list_song.append(song)
    print(song)
dl.download(list_song)