import requests
from bs4 import BeautifulSoup

def read_time(url: str, wpm: int) -> str:
    # check url for schema
    if "://" in url: pass
    else: url = "https://" + url
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'lxml')

    # remove headers, footers, styles, scripts
    try:
        for tag in ['header','footer', 'style', 'script']:
            s = soup.find(tag)
            s.decompose() 
    except: pass

    text = soup.get_text()
    num_words = len(text.split())

    read_time_min = num_words / wpm
    read_time_sec = ( read_time_min % 1 ) * 60
    read_time = str(int(read_time_min)) + " minutes & " + str(int(read_time_sec)) + " seconds"
    return read_time
    #return text

# test
#url = "https://www.section.io/engineering-education/integrate-tailwindcss-into-flask/"
#url = "www.google.co.in"
#url = "https://www.browserstack.com/guide/top-css-frameworks"
#url = "https://medium.com/analytics-vidhya/text-mining-extracting-and-analyzing-all-my-blogs-on-machine-learning-b6983c7a608e"
#url = "https://www.theverge.com/23513418/bring-back-personal-blogging"
#url = "https://www.geeksforgeeks.org/python-try-except/" #fail
#url = "https://onsclom.bearblog.dev/functional-programming-how-and-why/"
#print(read_time(url, 245))