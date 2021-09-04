from bs4 import BeautifulSoup
import urllib.request

# Получаем html
req = urllib.request.urlopen('https://air-wars.ru/rashodniki/pirotehnika/')
html = req.read()

# Получаем тело с карточками товара
soup = BeautifulSoup(html, 'html.parser')
body = soup.find_all('div', class_='product-grid row')

for item in body:
    # title = item.find_all('h4', class_='name')
    # for i in title:
    #     grenade_name = i.get_text()
    #     print(grenade_name)
    price = item.find_all('div', class_='price')
    if item.find_all('span', class_='price-new') is True:
        pass
    else:
        for i in price:
            grenade_price = i.get_text().strip()
            # print(grenade_price)



