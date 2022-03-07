import requests
from bs4 import BeautifulSoup

r = requests.get('https://gizmodo.jp')
s = BeautifulSoup(r.text, 'html.parser')
print(s.text)