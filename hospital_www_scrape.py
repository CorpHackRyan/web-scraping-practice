import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup

baseurl = "https://www.nhs.uk"
url = '/service-search/find-a-dentist/location/results/london'

# ul => {class : 'nhsuk-list'}
# a => href

head_info = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:101.0) Gecko/20100101 Firefox/101.0'}
req = requests.get(baseurl + url, headers=head_info)
# print(req.url)
# print(req.content)

htmldata = req.content  # default is in bytes

# Show data type
print(type(htmldata.decode()))

# parse html byte data into variable
soup = BeautifulSoup(htmldata.decode(), 'html.parser')

# print the data inside the soup variable
print(soup.prettify())

# Extract all the ul tags with the attribute nshul-list
ultag = soup.find('ul', attrs={'class': 'nhsuk-list'})
print(ultag)

# we want all the anchor tags within the ul tags above
for anch_tag in ultag.find_all('a', attrs={'class': 'link'}):
    print(anch_tag.get_text())
    print(anch_tag['href'])

#div, attrs = {'class' : 'nhsuk-grid-column-two-thirds nhsuk-u-margin-bottom-5'}
arealink = {}
for anch in ultag.find_all('a', attrs={'class': 'link'}):
    arealink[anch.get_text()] = anch['href]']

# extracting info from arealink dict
for name, link in arealink.items():
    print(name, link)
    req = requests.get(link, headers=head_info)
    pagedata = req.content.decode()


print(arealink)

