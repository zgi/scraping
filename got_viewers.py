from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Game_of_Thrones'
response = urlopen(url).read()
soup = BeautifulSoup(response)
seasons = []
views = []
for row in soup.findAll('th', attrs={'scope': 'row'}):
    if row.find('a'):
        seasons.append(row.find('a'))

for elem in range(8):
    got_season_url = 'https://en.wikipedia.org' + seasons[elem]['href']
    got_html = urlopen(got_season_url).read()
    got_soup = BeautifulSoup(got_html)
    catch_tr = got_soup.findAll('tr', attrs={'class': 'vevent'})[0]
    catch_td = catch_tr.findAll('td')[5]
    view_str = str(catch_td.contents[0])
    try:
        nr = float(view_str)
        views.append(nr)
# vpisi 0 ce ni podatka
    except ValueError:
        views.append(0)

all_viewers = 0

for x in views:
    all_viewers += x

print "Ogledi prve epizode vseg serij Game of Thrones: %.2f milionov" % all_viewers