import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup

url = 'https://www.iplt20.com/stats/2022'
req = requests.get(url)

# 200 means we can successfully scrape the data
print(req.status_code)

# print the entire html content
# data is of type 'bytes', NOT string
print(req.content)

# export to html file with 'wb' as 'write bytes'
with open('ipl20.html', 'wb') as fobj:
    fobj.write(req.content)

# store the page into a variable
data = req.content
print(data)

# let's use beautiful soup to hash the data
# goto inspect element in browser, click on network, paste the url, and you get this information
# fetching without the table data
req = requests.get(url)
print(req.headers, req.cookies)

# fetching with table data // we didnt finish this
headers_info = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:101.0) Gecko/20100101 Firefox/101.0'}
req = requests.get(url, headers=headers_info)
print(req.status_code)

# assigning data from a html table and plop it into a dataframe
url = 'https://www.arraysolar.co.in/group/group_dec.php?flag=group'
req = requests.get(url)
print(req.status_code)

# if theres multiple tables in the html page, then you'll get a list of dataframes
with open('pagedata.html', 'wb') as fobj:
    fobj.write(req.content)





