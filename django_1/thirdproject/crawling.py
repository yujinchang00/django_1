import requests
from bs4 import BeautifulSoup

def get_songs() :
    req = requests.get('https://music.bugs.co.kr/chart')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    titles = soup.find_all("p", class_="title")
    artists = soup.find_all("p", class_="artist")

    title_list = []
    artist_list = []
    for title, artist in zip(titles, artists) :
        title_list.append(title.get_text().replace("\n", ""))
        artist_list.append(artist.get_text().replace("\n", ""))

    return title_list, artist_list