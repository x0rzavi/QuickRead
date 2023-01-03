import requests
from bs4 import BeautifulSoup

def words(url):
    # check url for schema
    if "://" in url: pass
    else: url = "https://" + url
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'lxml')

    # remove headers and footers
    try:
        for tag in ['header','footer']:
            s = soup.find(tag)
            s.extract() 
    except: pass

    text = soup.get_text()
    #return text
    return len(text.split())

# test
#url = "https://www.section.io/engineering-education/integrate-tailwindcss-into-flask/"
#url = "www.google.co.in"
#url = "https://www.browserstack.com/guide/top-css-frameworks"
#url = "https://medium.com/analytics-vidhya/text-mining-extracting-and-analyzing-all-my-blogs-on-machine-learning-b6983c7a608e"
#url = "https://www.theverge.com/23513418/bring-back-personal-blogging"
#url = "https://www.geeksforgeeks.org/python-try-except/"
url = "https://onsclom.bearblog.dev/functional-programming-how-and-why/"
print(words(url))