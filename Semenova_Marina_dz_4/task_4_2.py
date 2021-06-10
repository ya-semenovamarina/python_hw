import requests
from bs4 import BeautifulSoup

page = 'http://www.cbr.ru/scripts/XML_daily.asp'
source = requests.get(page).text
print(dir(source))

#def get_content(html):
    #soup = BeautifulSoup(html, 'html.parser')
    #items = soup.find_all('table', class_='data')




