import requests
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/list/ls050226586/'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')
# print(soup.prettify())

appUrl = 'https://www.imdb.com'

titles = soup.select('h3>a')
for title in titles:
    print(f"Movie - {title.get_text()}")
    title_url = f"{appUrl}{title.get('href')}"
    res = requests.get(title_url)
    soup = BeautifulSoup(res.content, 'html.parser')
    genre_header = soup.find("h4", text="Genres:")
    genres_a = genre_header.find_next_siblings("a")
    genres = []
    for genre in genres_a:
        genres.append(genre.get_text().strip())

    print(f"Genres: {genres}")
