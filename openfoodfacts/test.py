"""Download path progression from Openclassroom."""
import requests
from bs4 import BeautifulSoup

r = requests.get('http://coreyms.com').text
soup = BeautifulSoup(r, 'lxml')
article = soup.find('article')
print(article)
