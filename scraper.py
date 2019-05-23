import requests
import csv

#url = 'https://www.paginegialle.it/ricerca/ottica/Sezze%20(LT)/p-' + str(i)
name = []
phone = []
address = []
zipcode = []
city = []
province = []
pages = []
from bs4 import BeautifulSoup

for i in range(1,4):
    url = 'https://www.paginegialle.it/ricerca/ottica/Sezze%20(LT)/p-' + str(i)
    pages.append(url)

for item in pages:
    page = requests.get(item)
    soup = BeautifulSoup(page.text, 'html.parser')
    sectionTag = soup.find_all('section', class_='vcard')

    #name
    for x in soup.find_all('header', class_=None):
        name.append(x.find('a', class_=None).text.lstrip().rstrip())
    #phone
    for tag in sectionTag:
        spanTags = tag.find_all('span', class_='phone-label')
        for tag in spanTags:
            phone.append(tag.text.replace(',', ''))
    #address
    for x in soup.find_all('div', class_='street-address'):
        address.append(x.find(class_=None).text)
    #ZIP
    for x in soup.find_all('span', class_='postal-code'):
        zipcode.append(x.text)
    #city
    for x in soup.find_all('span', class_='locality'):
        city.append(x.text)
    #province
    for x in soup.find_all('span', class_='region'):
        province.append(x.text.replace('(', '').replace(')', ''))

rows = zip(name,phone,address,city,zipcode,province)
with open('prova.csv', "w") as f:
    writer = csv.writer(f)
    for row in rows:
        writer.writerow(row)
