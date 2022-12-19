from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
article_tag = soup.find(class_="titleline")
article_text = article_tag.getText()
article_link = article_tag.get("href")
article_upvote = soup.find(name="span", class_="score").getText()

print(article_text)
print(article_link)
print(article_upvote)