from bs4 import BeautifulSoup
import lxml
import requests
from pprint import pprint

response = requests.get('https://news.ycombinator.com/news')
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
pprint(soup.title)
article_tag = soup.find("a", "titlelink")
article_text= article_tag.getText()
article_link =article_tag.get("href")
article_upvote =soup.find(name="span", class_="score")
print(article_tag)
print(article_text)
print(article_upvote.getText())
print(article_link)