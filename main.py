from lxml import html
import requests
import operator

page = requests.get('http://www.soundscapesmusic.com/tickets/')
tree = html.fromstring(page.content)
gigs = tree.xpath('//tr[position()>1]//td')
calendar = {'Jan': 1,'Feb': 2,'Mar': 3,'Apr': 4,
            'May': 5,'Jun': 6,'June': 6,'Jul': 7,'Aug': 9,
            'Sep': 9,'Oct': 10,'Nov': 11,'Dec': 12}
data = []
artists = []
locations = []
dates = []
prices = []

def getData():
    for i in range(0,len(gigs),4):
        artist = gigs[i].text_content()
        location = gigs[i+1].text_content()
        d = gigs[i+2].text_content()
        date = d.split(" ")
        month = getMonth(date)
        day = getDay(date)
        price = gigs[i+3].text_content()
        deets = [artist, location, date, price,month,int(day)]
        data.append(deets)

def getMonth(date):
    if len(date) > 2:
        if date[1] in calendar:
            return calendar[date[1]]
    else:
        return calendar[date[0]]

def getDay(date):
    if len(date) > 2:
        day = date[2].split("-")
        return day[0]
    else:
        day = date[1].split("-")
        return day[0]

def sortByArtists(data):
    data.sort(key=operator.itemgetter(0))
    return data

def sortByDate(data):
    sortedDataTemp = sorted(data, key=operator.itemgetter(4,5,3,0))
    return sortedDataTemp:

def sortByPrice(data):
    data.sort(key=operator.itemgetter(3))
    return data

getData()
