import requests
from bs4 import BeautifulSoup, SoupStrainer

url = "https://matix.io/extract-text-from-webpage-using-beautifulsoup-and-python/"
html = requests.get(url)
soup = BeautifulSoup(html.text, 'lxml')

text = soup.get_text()
print(len(text.split()))