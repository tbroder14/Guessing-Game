import requests
from bs4 import BeautifulSoup

url = 'https://www.nfl.com/'
html = requests.get(url)
print(html)

soup = BeautifulSoup(html.content, 'html.parser')

s = soup.find('ol', class_='nfl-o-headlinestack__list')
lines = s.find_all('span', class_='nfl-o-headlinestack__item-text')

for line in lines:
    print(line.contents)
