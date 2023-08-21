from bs4 import BeautifulSoup
import requests

amazon_text = requests.get('https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_1').text
soup = BeautifulSoup(amazon_text, 'lxml')
all_div = soup.find_all('div', class_='sg-col-inner')
for products in all_div:
    title = products.find('span', class_='a-size-medium a-color-base a-text-normal').text
    rating = products.find('span', class_='a-size-base puis-normal-weight-text:').text
    review = products.find('span', class_='a-size-base s-underline-text').text
    price = products.find('span', class_='a-offscreen').text
    url = products.find('a', class_='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal').text

    print(title)
    print(rating)
    print(review)
    print(price)
    print(url)




