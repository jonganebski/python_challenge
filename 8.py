# http://www.pythonchallenge.com/pc/def/integrity.html

from bs4 import BeautifulSoup
import requests
import re
URL = 'http://www.pythonchallenge.com/pc/def/integrity.html'

request = requests.get(URL)
html = BeautifulSoup(request.text, 'html.parser')
# print(html)
area_cords = html.find_all('area')
area_cords = str(area_cords)
cords_nums = re.findall('\d+', area_cords)
print(cords_nums)
pw = ''
for n in cords_nums:
    pw += (chr(int(n)))
print(pw)
