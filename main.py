from bs4 import BeautifulSoup
import lxml
import requests
from pprint import pprint

response = requests.get('https://news.ycombinator.com/news')
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
#pprint(soup.title)
articles = soup.find_all("a", "titlelink")
#pprint(articles)
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

#article_upvotes = [score.getText() for score in soup.find_all(name="span", class_="score")]
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
#pprint(article_texts)
#pprint(article_links)
print(article_upvotes)
highest = max(article_upvotes)
the_index = article_upvotes.index(highest)
print(article_links[the_index])
print(article_texts[the_index])