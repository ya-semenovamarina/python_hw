from urllib.request import urlopen
from xml.etree import ElementTree as etree

with urlopen("http://www.cbr.ru/scripts/XML_daily.asp") as r:
    USD_currency = print('USD', etree.parse(r).findtext('.//Valute[@ID="R01235"]/Value'))
with urlopen("http://www.cbr.ru/scripts/XML_daily.asp") as r:
    EUR_currency = print('EUR', etree.parse(r).findtext('.//Valute[@ID="R01239"]/Value'))