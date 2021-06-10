from urllib.request import urlopen
from xml.etree import ElementTree as etree

with urlopen("http://www.cbr.ru/scripts/XML_daily.asp", timeout=10) as r:
    USD_currency = print(etree.parse(r).findtext('.//Valute[@ID="R01235"]/Value'))
with urlopen("http://www.cbr.ru/scripts/XML_daily.asp", timeout=10) as r:
    EUR_currency = print(etree.parse(r).findtext('.//Valute[@ID="R01239"]/Value'))