import requests
import lxml
from bs4 import BeautifulSoup

url = "https://www.amazon.ca/Windows-Mini-Single-Board-Computer/dp/B0BDFDTCD4/ref=sr_1_2?crid=1J27JDM0EUFRO&keywords=lattepanda&qid=1671687865&sprefix=latte+panda%2Caps%2C178&sr=8-2"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.2 Safari/605.1.15",
    "Accept-Language": "en-CA,en-US;q=0.9,en;q=0.8"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
print(soup.prettify())

price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)