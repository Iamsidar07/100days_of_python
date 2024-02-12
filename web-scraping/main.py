from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
contents = response.text

soup = BeautifulSoup(contents, "html.parser")

articles = soup.select(selector=".titleline>a")
article_titles = []
article_links = []
for article_tag in articles:
    title = article_tag.getText()
    article_titles.append(title)
    link = article_tag.get("href")
    article_links.append(link)

article_upvotes = [
    int(score.getText().split()[0])
    for score in soup.find_all(name="span", class_="score")
]

max_upvote_index = article_upvotes.index(max(article_upvotes))
top_article_title = article_titles[max_upvote_index]
top_article_link = article_links[max_upvote_index]

print(max_upvote_index, top_article_title, top_article_link)

# with open("./website.html") as html_file:
#     contents = html_file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# print(soup.title.string)
# print(soup)
