# http://www.pythonchallenge.com/pc/def/peak.html

import urllib.request
import pickle

read_file = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/banner.p').read()

open_file = pickle.loads(read_file)

for i in open_file:
    print('\n')
    line = ''
    for tuple in i:
      line += tuple[0] * tuple[1]
    print(line)

