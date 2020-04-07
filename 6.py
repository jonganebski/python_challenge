# http://www.pythonchallenge.com/pc/def/channel.html

import urllib.request
import pickle

read_file = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/banner.p').read()
open_file = pickle.loads(read_file)

def seperate():
  all = []
  for i in open_file:
    list = []
    for t in i:
      list.append(t[0])
      list.append(t[1])
    all.append(list)
  return all

def pair(all):
  all_list = []
  for i in all:
    line = []
    if len(i) <= 2:
        line = [tuple(i)]
    else:
      for n in range(len(i)-2):
        line += [(i[n], i[n+1])]
    all_list.append(line)
  return all_list

all = seperate()

for i in pair(all):
  # print(i)
  print('\n')
  line = ''
  for tuple in i:
    line += tuple[0] * tuple[1]
  print(line)
