import codecs
from bs4 import BeautifulSoup

csv = open("./data.csv", "a+")

html_raw = codecs.open("./index.html", 'r')
html = html_raw.read()

soup = BeautifulSoup(html, features="html.parser")

heading = ""
for header in soup.find_all("th"):
    heading += (header.text+",")
heading = heading[:-1]
heading = heading+"\n"

csv.write(heading)

rows = []
for row in soup.find_all("tr"):
    cols = row.find_all("td")
    op_row = []
    for i in range(len(cols)):
        temp = cols[i].text
        if("an" in temp and i == 0):
            break
        else:
            op_row.append(temp)
    if(len(op_row) != 0):
        rows.append(op_row)
        op_row = []


for row in rows:
    line = ""
    for item in row:
        line += "\"" + item + "\","
    line = line[:-1]
    line += "\n"
    csv.write(line)

csv.close()
