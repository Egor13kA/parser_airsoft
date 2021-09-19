from bs4 import BeautifulSoup
import urllib.request
import classes


# Получаем html
req = urllib.request.urlopen('https://air-wars.ru/rashodniki/pirotehnika/')
html = req.read()
# Получаем soup с карточками товара
soup = BeautifulSoup(html, 'html.parser')

# Вызываем парсер сайта air-wars.ru, ищем гранаты.
gren = classes.airwars(soup).grenade_airwars()
# Записываем в БД
classes.insert_gren(gren)

