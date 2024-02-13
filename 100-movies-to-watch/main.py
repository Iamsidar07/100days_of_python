import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL)
contents = response.text

soup = BeautifulSoup(contents, "html.parser")
title_tags = soup.find_all(name="h3", class_="title")
title_tags.reverse()
with open("movies.txt", mode="w") as file:
    for title_tag in title_tags:
        title_text = title_tag.getText()
        if title_text.find(")") != -1:
            title_tag_list = title_text.split(")")
        else:
            title_tag_list = title_text.split(":")
        movie_title = title_tag_list[1].strip()
        serial_number = title_tag_list[0]
        file.write(f"{serial_number}) {movie_title}\n")
