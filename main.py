from bs4 import BeautifulSoup
import urllib.request
import classes

iteration_count = 4

for item in range(1,5):
    # Получаем html
    req = urllib.request.urlopen(f'https://air-wars.ru/rashodniki/pirotehnika/?page={item}')
    html = req.read()
    # Получаем soup с карточками товара
    soup = BeautifulSoup(html, 'html.parser')
    # Вызываем парсер сайта air-wars.ru, ищем гранаты.
    gren = classes.airwars(soup).grenade_airwars()
    # Записываем в БД
    classes.insert_gren(gren)





