import sqlite3
from bs4 import BeautifulSoup
import datetime
import requests

reponse = requests.get('https://ua.sinoptik.ua/')
reponse_text = reponse.text

date_now = datetime.datetime.now()
soup = BeautifulSoup(reponse_text, features='html.parser')
soup_l = soup.find_all('p', {'class': 'today-temp'})
res = soup_l[0].text

#cur.execute('CREATE TABLE weather (date DATATIME, time TEXT)')

connection = sqlite3.connect('it_step_DB.sl3', 5)
cur = connection.cursor()

cur.execute(f'INSERT INTO weather (date, time) VALUES ("{date_now}", "{res}")')

connection.commit()
connection.close()
