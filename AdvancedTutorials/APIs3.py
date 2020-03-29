from urllib import request
from bs4 import BeautifulSoup
import json
import csv

#Sample page for practice
page_url = 'http://alansimpson.me/python/scrape_sample.html'
#Open page
raw_page = request.urlopen(page_url)
#Make a beautiful soup object out of that html [page]
soup = BeautifulSoup(raw_page, 'html5lib')

#Isolate the main content block
content = soup.article

#Create an empty list for the dictionary items
links_list = []

#Loop through all the links in the article
for link in content.find_all('a'):
    # try to get the href, image url and text
    try:
        url = link.get('href')
        img = link.img.get('src')
        text = link.span.text
        links_list.append({'url': url, 'img': img, 'text': text})
    # If the row is missing anything....
    except AttributeError:
        # Skip it, don't blow it up
        pass

#Save it to a JSON file
with open('links.json', 'w', encoding='utf-8') as links_file:
    json.dump(links_list, links_file, ensure_ascii=False)

#Save it to a csv
with open('links.csv', 'w', newline='') as csv_out:
    csv_writer = csv.writer(csv_out)
    #Create the header row
    csv_writer.writerow(['url', 'img', 'text'])
    for row in links_list:
        csv_writer.writerow([str(row['url']), str(row['img']), str(row['text'])])

print('Done')
