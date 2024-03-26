import requests
import bs4

URL = 'https://cs111.byu.edu'
response = requests.get(URL)

print(response.status_code)

soup = bs4.BeautifulSoup(response.text,'html.parser')

for item in soup.body.children:
    print(type(item))
print(soup.title)
print(soup.title.attrs)

for p_tag in soup.find_all('p'):
    print(p_tag.prettify())