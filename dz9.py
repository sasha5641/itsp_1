import requests
from bs4 import BeautifulSoup

response = requests.get('https://bank.gov.ua/ua/markets/exchangerates')
response_text = response.text

soup = BeautifulSoup(response_text, features='html.parser')
soup_list = soup.find_all('td', {'data-label': 'Офіційний курс'})
res = soup_list[7].text
print(res)