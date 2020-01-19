import requests
from bs4 import BeautifulSoup

# Setting the url to the destination site
URL = 'https://www.madewell.com/womens/clothing/sweaters'

# Getting source and parsing content with BS4
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

# Getting all clothing with products objects
results = soup.find(id="search-result-content")
price = results.find_all('div', class_='product-pricing')

# Getting and printing price for each clothing product
for price in price:
    s = price.find_all('span')

    for span in s:
        print(span.text)