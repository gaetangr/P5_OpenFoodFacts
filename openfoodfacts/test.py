""" Download path progression from Openclassroom """
from bs4 import BeautifulSoup
import requests

r = requests.get('http://coreyms.com').text
soup = BeautifulSoup(r, 'lxml')
article = soup.find('article')
print(article)