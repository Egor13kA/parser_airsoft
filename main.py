from bs4 import BeautifulSoup
import urllib.request
from classes import airwars
import sqlite3

# Получаем html
req = urllib.request.urlopen('https://air-wars.ru/rashodniki/pirotehnika/')
html = req.read()
# Получаем soup с карточками товара
soup = BeautifulSoup(html, 'html.parser')

# Вызываем парсер сайта air-wars.ru, ищем гранаты.
gren = airwars(soup)

# Записываем данные в БД
db = sqlite3.connect('parsing_airsoft.db')
cursor = db.cursor()

cursor.executemany('INSERT INTO agrenade (name, price, instock) VALUES (?, ?, ?)', gren.grenade_airwars())
db.commit()

db.close()


# print(gren.grenade_airwars())
