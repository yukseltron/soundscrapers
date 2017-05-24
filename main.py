from lxml import html
import requests

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
