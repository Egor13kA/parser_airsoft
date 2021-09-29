from bs4 import BeautifulSoup
import urllib.request
import sqlite3


def soup_grenade_airwars(page_number):
    # Получаем html
    req = urllib.request.urlopen(f'https://air-wars.ru/rashodniki/pirotehnika/?page={page_number}')
    html = req.read()

    # Получаем soup с карточками товара
    soup = BeautifulSoup(html, 'html.parser')
    return soup


def soup_bb_airwars(page_number):
    # Получаем html
    req = urllib.request.urlopen(f'https://air-wars.ru/rashodniki/shary/?page={page_number}')
    html = req.read()

    # Получаем soup с карточками товара
    soup = BeautifulSoup(html, 'html.parser')
    return soup


def insert_gren(iter_obj):
    db = sqlite3.connect('parsing_airsoft.db')
    cursor = db.cursor()
    # Запись\обновление значений в БД
    for dict_gren in iter_obj:
        cursor.execute('''INSERT INTO agrenade (name, price, instock) VALUES (?, ?, ?)
                        ON CONFLICT (name) DO UPDATE SET price=?, instock=?''',
                       (dict_gren.get('title'),
                        dict_gren.get('price'),
                        dict_gren.get('instock'),
                        dict_gren.get('price'),
                        dict_gren.get('instock')
                        )
                       )
        db.commit()
    db.close()


def insert_bbs(iter_obj):
    db = sqlite3.connect('parsing_airsoft.db')
    cursor = db.cursor()
    # Запись\обновление значений в БД
    for dict_it in iter_obj:
        cursor.execute('''INSERT INTO abbs (name, price, instock) VALUES (?, ?, ?)
                            ON CONFLICT (name) DO UPDATE SET price=?, instock=?''',
                       (dict_it.get('title'),
                        dict_it.get('price'),
                        dict_it.get('instock'),
                        dict_it.get('price'),
                        dict_it.get('instock')
                        )
                       )
        db.commit()
    db.close()


class airwars:
    def __init__(self):
        self.grenade = []
        self.bbs = []

    # Парсинг гранат
    # Получаем наименование, цену, наличие (0 - нет, 1 - в наличии)
    def grenade_airwars(self, soup):

        for item in soup.find('div', class_='product-grid row').find_all('div', class_='col-sm-3 box-product'):
            title = item.h4.a.get_text()

            # Выбор актуальной цены
            if item.find(class_='price-new') is None:
                price = item.find('div', class_='price').get_text(strip=True)
            else:
                price = item.find(class_='price-new').get_text(strip=True)
            price_int = ''.join(filter(lambda price: price.isdigit(), price))
            # Проверка наличия
            if item.find('input', class_='button') is None:
                instock = 0
            else:
                instock = 1
            self.grenade.append({'title': title, 'price': price_int, 'instock': instock})
        return self.grenade

    # Парсинг шаров
    # Получаем наименование, цену, наличие (0 - нет, 1 - в наличии)

    def bb_airwars(self, soup):
        bb = []

        for item in soup.find('div', class_='product-grid row').find_all('div', class_='col-sm-3 box-product'):
            # Название
            title = item.h4.a.get_text()

            # Выбор актуальной цены
            if item.find(class_='price-new') is None:
                price = item.find('div', class_='price').get_text(strip=True)
            else:
                price = item.find(class_='price-new').get_text(strip=True)
            price_int = ''.join(filter(lambda price: price.isdigit(), price))
            # Проверка наличия
            if item.find('input', class_='button') is None:
                instock = 0
            else:
                instock = 1

            self.bbs.append({'title': title, 'price': price_int, 'instock': instock})
        return self.bbs
