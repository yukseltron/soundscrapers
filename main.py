from lxml import html
import requests
import operator

page = requests.get('http://www.soundscapesmusic.com/tickets/')
tree = html.fromstring(page.content)

gigs = tree.xpath('//tr[position()>1]//td')
data = []
artists = []
locations = []
dates = []
prices = []

for i in range(0,len(gigs),4):
    artist = gigs[i].text_content()
    location = gigs[i+1].text_content()
    date = gigs[i+2].text_content()
    price = gigs[i+3].text_content()

    deets = [artist, location, date, price]
    data.append(deets)

def sortByArtists(data):
    data.sort(key=operator.itemgetter(0))
    for i in data:
        print(i)

def sortByDate(data):
    data.sort(key=operator.itemgetter(2))
    for i in data:
        print(i)

def sortByPrice(data):
    data.sort(key=operator.itemgetter(3))
    for i in data:
        print(i)

sortByDate(data)
