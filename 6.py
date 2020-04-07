# http://www.pythonchallenge.com/pc/def/channel.html

import zipfile
import re

# myzip = zipfile.ZipFile('channel.zip').read()
# print(myzip)

# num = 90052
# for i in range(10):
#   textfile = f'{num}.txt'
#   with zipfile.ZipFile('channel.zip') as myzip:
#   # with myzip.open('readme.txt') as myfile: #from 90052  
#     with myzip.open(textfile) as myfile:
#     # with myzip.open('94191.txt') as myfile:
#       text = str(myfile.read())
#       num = re.findall('\d+', text)
#       print(num)
#       print(text) # b'Next nothing is 94191'

channel = zipfile.ZipFile('channel.zip')
num = 90052
for i in range(1000):
  text = channel.read(f'{num}.txt')
  text = str(text.decode('utf-8'))
  num_list = re.findall('\d+', text)
  if num_list == []:
    print(text)
    break
  else:
    num = num_list[0]
    print(text)
  # print(num)
