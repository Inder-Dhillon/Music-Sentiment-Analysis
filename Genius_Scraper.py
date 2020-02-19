from requests import get
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import lxml
import html2text


def find_song(song_name, artist):
    token = "Bearer token_here"
    genius_search = "http://api.genius.com/search?q=" + "%20".join(song_name.split(" ")) + "%20" + "%20".join(
        artist.split(" "))
    Header = {
        "Authorization": token
    }
    res = get(genius_search, headers=Header).json()
    return (res['response']['hits'][0]['result']['url'])

def get_lyrics(url):
    only_div = SoupStrainer('div', {"class": "lyrics"})
    scrape = get(url).text
    soup = BeautifulSoup(scrape, 'lxml', parse_only=only_div)
    return (html2text.html2text(soup.text))

print(get_lyrics(find_song(title, artist)))