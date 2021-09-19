import sqlite3


class airwars:

    def __init__(self, soup):
        self.soup = soup

    # Получаем наименование, цену, наличие (0 - нет, 1 - в наличии)
    def grenade_airwars(self):
        grenade = []

        for item in self.soup.find('div', class_='product-grid row').find_all('div', class_='col-sm-3 box-product'):
            title = item.h4.a.get_text()

            # Выбор актуальной цены
            if item.find(class_='price-new') is None:
                price = item.find('div', class_='price').get_text(strip=True)
            else:
                price = item.find(class_='price-new').get_text(strip=True)
            # Проверка наличия
            if item.find('div', class_='cart') is None:
                instock = 0
            else:
                instock = 1
            grenade.append({'title': title, 'price': price.replace(' p.', ''), 'instock': instock})
        return grenade


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

