import requests
from bs4 import BeautifulSoup

resp = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
soup = BeautifulSoup(resp.content, "xml")
# print(soup.prettify())

print(soup.find('CharCode', text='EUR').find_next_sibling('Value').string)

print(soup.find(ID="R01239").Value.string)

resp = requests.get(
    "http://api.openweathermap.org/data/2.5/weather",
    params={
    "q": "Almaty",
    "APPID": "7543b0d800ce423bab3b2f6ad38df30b",
    'mode': 'xml', 'units': 'metric'
    }
)
  
soup = BeautifulSoup(resp.content, "xml")
print(soup.temperature['value'])




