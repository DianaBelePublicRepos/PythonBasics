#Import de request URl from the urllib library.
from urllib import request
#handy tool for scraping a web page
from bs4 import BeautifulSoup

page_url = 'http://alansimpson.me/python/scrape_sample.html'
#Open the page
rawpage = request.urlopen(page_url)

#Make a beautiful soup
soup = BeautifulSoup(rawpage, 'html5lib')

#Isolate the main content block
content = soup.article

#Create an empty list for dictionary items.
links_list = []
#Loop through all the links in the article
for link in content.find_all('a'):
    #try to get the href, image url and text
    try:
        url = link.get('href')
        img = link.img.get('src')
        text = link.span.text
        links_list.append({'url': url, 'img': img, 'text': text})
    #If the row is missing anything....
    except AttributeError:
        #Skip it, don't blow it up
        pass

