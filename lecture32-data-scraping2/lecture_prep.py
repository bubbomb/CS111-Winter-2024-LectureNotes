import requests
import bs4

html = '''
<html>
<table id="degrees" border="1">
  <tr><th>Academic Year</th><th>Bachelors</th>
      <th>Masters</th><th>Doctoral</th><th>Total</th></tr>
  <tr><td>2021-2022</td><td>6406</td>
      <td>1128</td><td>233</td><td>7767</td></tr>
  <tr><td>2020-2021</td><td>6683</td><td>959</td>
      <td>192</td><td>7834</td></tr>
  <tr><td>2019-2022</td><td>6684</td>
      <td>1033</td><td>212</td><td>7929</td></tr>
...
  <tr><td>1896-1897</td><td>1</td>
      <td>0</td><td>0</td><td>1</td></tr>
</table>
</html>
'''
soup = bs4.BeautifulSoup(html, 'html.parser')

table = soup.find('table', {'id':'degrees'})
heads = table.find_all('th')
headers = []
for item in heads:
    headers.append(item.string)
data = [[], [], [], [], []]   # make a list of 5 lists, one for each column
rows = table.find_all('tr')
for row in rows:
    columns = row.find_all("td")
    index = 0
    for col in columns:
        data[index].append(col.string)
        index += 1
for col in data:
    print(col)