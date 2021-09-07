from bs4 import BeautifulSoup
import urllib.request

# Получаем html
req = urllib.request.urlopen('https://air-wars.ru/rashodniki/pirotehnika/')
html = req.read()

# Получаем soup с карточками товара
soup = BeautifulSoup(html, 'html.parser')

grenade = []

# Получаем наименование и цену
for item in soup.find_all('div', class_='col-sm-3 box-product'):
    title = item.h4.a.get_text()
    price = item.find('div', class_='price').get_text(strip=True)
    print(title)
    print(price)
