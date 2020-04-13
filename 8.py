# http://www.pythonchallenge.com/pc/def/integrity.html

from bs4 import BeautifulSoup
import requests
import re
URL = 'http://www.pythonchallenge.com/pc/def/integrity.html'

request = requests.get(URL)
html = BeautifulSoup(request.text, 'html.parser')
#  print(html)
# area_cords = html.find_all('area')
# area_cords = str(area_cords)
# cords_nums = re.findall('\d+', area_cords)
# print(cords_nums)
# pw = ''
# for n in cords_nums:
#     pw += (chr(int(n)))
# print(pw)

soup_comment = html.find_all(string = lambda text: isinstance(text, Comment))
print(soup_comment)
un = 'BZh91AY&SYA\\xaf\\x82\\r\\x00\\x00\\x01\\x01\\x80\\x02\\xc0\\x02\\x00 \\x00!\\x9ah3M\\x07<]\\xc9\\x14\\xe1BA\\x06\\xbe\\x084'
pw = 'BZh91AY&SY\\x94$|\\x0e\\x00\\x00\\x00\\x81\\x00\\x03$ \\x00!\\x9ah3M\\x13<]\\xc9\\x14\\xe1BBP\\x91\\xf08'
print(ord('\\xaf'))
