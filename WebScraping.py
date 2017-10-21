# import the requests library
import requests
from bs4 import BeautifulSoup
import csv
# specify the url of the webpage you want to scrape
URL = "http://www.values.com/inspirational-quotes"
#send html requests to the specified URL and save
#the response from server in a response object r
r = requests.get(URL)
#print the content to get the raw html
#print(r.content)
# create beautiful soap by passing two arguments
#r.content --> raw html content
#html5lib--> html parser
soup = BeautifulSoup(r.content,'html5lib')
# visual representation of the parse tree created
#print(soup.prettify())
quotes = [] # a list to store quotes
table = soup.find('div',attrs={'id':'container'})

for row in table.findAll('div',attrs={'class':'quote'}):
    quote={}
    quote['theme'] = row.h5.text
    quote['url'] = row.a['href']
    quote['img'] = row.img['src']
    quote['lines'] = row.h6.text
    quote['author'] = row.p.text
    quotes.append(quote)

filename = 'inspirational_quotes.csv'
with open(filename, 'wb') as f:
    w = csv.DictWriter(f,['theme','url','img','lines','author'])
    w.writeheader()
    for quote in quotes:
        w.writerow(quote)
