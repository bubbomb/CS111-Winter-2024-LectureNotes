import requests
import bs4

URL = 'https://cs111.byu.edu'
response = requests.get(URL)


soup = bs4.BeautifulSoup(response.text, 'html.parser')


# print(soup.title)
# print(soup.p)
# print(soup.tr)

# for a_tag in soup.find_all('a'):
#     print(a_tag.attrs)
#     print(a_tag.attrs['href']kkkkkk
# print(soup.body.children)

# for child in soup.ul.children:
#     print(child)

# print(soup.a)
# print('------------------')
# print(soup.a.parent)

# print(soup.find_all('tr', class_='week-header'))

print(soup.a.prettify())