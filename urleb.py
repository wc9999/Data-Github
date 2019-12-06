from bs4 import BeautifulSoup
import requests


sumber = requests.get('https://github.com/').text

sop = BeautifulSoup(sumber, 'lxml')

articles = sop.find('header')

print(articles.prettify())