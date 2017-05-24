from lxml import html
import requests

page = requests.get('http://www.soundscapesmusic.com/tickets/')
tree = html.fromstring(page.content)
