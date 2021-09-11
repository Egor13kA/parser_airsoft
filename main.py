from bs4 import BeautifulSoup
import urllib.request

# Получаем html
req = urllib.request.urlopen('https://air-wars.ru/rashodniki/pirotehnika/')
html = req.read()

# Получаем soup с карточками товара
soup = BeautifulSoup(html, 'html.parser')

grenade = []

# Получаем наименование и цену

for item in soup.find('div', class_='product-grid row').find_all('div', class_='col-sm-3 box-product'):
    title = item.h4.a.get_text()
    # Выбор актуальной цены
    if item.find(class_='price-new') == None:
        price = item.find('div', class_='price').get_text(strip=True)
    else:
        price = item.find(class_='price-new').get_text(strip=True)

    grenade.append({
       'title': title,
       'price': price.replace(' p.', '')
    })
    # print(title)
    # print(price)

print(grenade)