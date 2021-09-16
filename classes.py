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
            if item.find('div', class_='cart') is None:
                instock = 0
            else:
                instock = 1

            product = (title, price.replace(' p.', ''), instock)
            grenade.append(product)
        return grenade

