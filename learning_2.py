from bs4 import BeautifulSoup
import lxml
import requests
from pprint import pprint

response = requests.get('https://news.ycombinator.com/news')
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
pprint(soup.title)
articles = soup.find_all("a", "titlelink")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

    article_upvote = soup.find_all(name="span", class_="score")

print(article_tag)
print(text)
print(article_upvote.getText())
print(link)