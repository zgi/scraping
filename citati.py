from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup
import random

url = 'https://quotes.yourdictionary.com/theme/marriage/'
response = urlopen(url).read()
soup = BeautifulSoup(response)
quotes = []
selected_quotes = []

for link in soup.findAll('p', attrs={"class": "quoteContent"}):
    quotes.append(link.string)

while len(selected_quotes) <5:
    rand_index = random.randrange(len(quotes))
    if quotes[rand_index] not in selected_quotes:
        selected_quotes.append(quotes[rand_index])

for index, quote in enumerate(selected_quotes):
    quote_strip_ = str(quote).lstrip(' ')
    print "%d : %s " % (index, quote_strip_)