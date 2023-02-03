import cfscrape
import requests
from bs4 import BeautifulSoup

scraper = cfscrape.create_scraper()
response = scraper.get('https://www.in.gov.br/leiturajornal')

if response.status_code == 200:
    print('Code sucesso')
else:
    print('Deu bo')

soup = BeautifulSoup(response.content, 'html.parser')


secao = soup.find_all("h5", class_="title-marker")
date = soup.find('li', class_="breadcrumb-item publication-info-marker")
print(date)