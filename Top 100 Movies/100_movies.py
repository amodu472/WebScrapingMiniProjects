from bs4 import BeautifulSoup
import requests

movies_site = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(url=movies_site)
movies_data = response.text

# the scraping part below
soup = BeautifulSoup(movies_data, "html.parser")
titles = soup.select(selector="h3.title")
titles_text = [movie.getText() for movie in titles[::-1]]

with open("top100.txt", mode="w") as movies_file:
    for title in titles_text:
        if '59' in title:
            movies_file.write("59) E.T. - The Extra Terrestrial\n")
        else:
            movies_file.write(f"{title}\n")
