from bs4 import BeautifulSoup
import urllib.request
import os, sys
import webbrowser
href = []

def YoutubeSearch(Query):
    url = "https://www.youtube.com/results?search_query=!_INPUT_!"
    url = url.replace("!_INPUT_!", Query)
    with urllib.request.urlopen(url) as response:
        html = response.read()
    Soup = BeautifulSoup(html, 'html.parser')
    for link in Soup.find_all('a', {'class' : 'yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink spf-link '}):
        href.append(link.get('href'))
    video = (('http://www.youtube.com_HREF_')
             .replace('_HREF_', href[0]))
    webbrowser.open(video)
