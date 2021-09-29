from classes import *

a = airwars()
# Вызываем парсер сайта air-wars.ru, ищем гранаты.
for i in range(1, 5):
    site = soup_grenade_airwars(i)
    a.grenade_airwars(site)

# Записываем в БД
insert_gren(a.grenade)

# Вызываем парсер сайта air-wars.ru, ищем шары
for i in range(1, 4):
    site = soup_bb_airwars(i)
    a.bb_airwars(site)

# Записываем в БД
insert_bbs(a.bbs)

