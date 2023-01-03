import requests
from bs4 import BeautifulSoup, SoupStrainer

url = "https://startafuckingblog.com/"
html = requests.get(url)
soup = BeautifulSoup(html.text, features="lxml")

text = soup.get_text()
print(len(text.split()))