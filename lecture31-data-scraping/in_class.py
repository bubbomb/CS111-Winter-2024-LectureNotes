import requests
import bs4
import re

URL = 'https://cs111.byu.edu/staff'
response = requests.get(URL)


soup = bs4.BeautifulSoup(response.text, 'html.parser')

name_regex = re.compile(r'.*Ste.*')
tags = soup.find_all(['img', 'h3'])
print(tags)