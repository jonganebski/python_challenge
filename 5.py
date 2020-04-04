# http://www.pythonchallenge.com/pc/def/peak.html

import urllib.request
import pickle

read_file = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/banner.p').read()

open_file = pickle.loads(read_file)

for i in open_file:
    print(i)
