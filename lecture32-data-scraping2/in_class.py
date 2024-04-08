import requests
import bs4

html = '''
<html>
<table id="degrees" border="1">
    <thead> 
    <tr><th>Academic Year</th><th>Bachelors</th>
        <th>Masters</th><th>Doctoral</th><th>Total</th></tr>
    </thead>
    <tr><td>2021-2022</td><td>6406</td>
        <td>1128</td><td>233</td><td>7767</td></tr>
    <tr><td>2020-2021</td><td>6683</td><td>959</td>
        <td>192</td><td>7834</td></tr>
    <tr><td>2019-2022</td><td>6684</td>
        <td>1033</td><td>212</td><td>7929</td></tr>
    <tr><td>1896-1897</td><td>1</td>
        <td>0</td><td>0</td><td>1</td></tr>
</table>

<table> </table>
</html>
'''
soup = bs4.BeautifulSoup(html, 'html.parser')

table = soup.find('table', {'id': 'degrees'})

html_headers = table.find_all('th')

python_headers = []
for header in html_headers:
    python_headers.append(header.text)

print(python_headers)

python_data = [[],[],[],[],[]]

table_rows = table.find_all('tr')

for row in table_rows:
    columns = row.find_all("td")
    index = 0
    for col in columns:
        python_data[index].append(col.string)
        index += 1

print(python_data)

