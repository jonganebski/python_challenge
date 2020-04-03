# http://www.pythonchallenge.com/pc/def/linkedlist.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345
# and the next nothing is 44827
# and the next nothing is 45439
# Your hands are getting tired and the next nothing is 94485

import urllib.request
from bs4 import BeautifulSoup

num_str = '12345'

for x in range(400):
  request = urllib.request.urlopen(f'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={num_str}')
  soup = BeautifulSoup(request, 'html.parser')
  print(soup)
  
  num_str = ''

  for i in str(soup):
    if i.isdigit() is True:
      num_str += i
