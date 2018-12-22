from itertools import product
from string import *

keywords = [''.join(i) for i in product("0"+"1"+"2"+"3", repeat =  4)]
file = open("file.txt", "w")

for item in keywords: 
  file.write("%s\n" % item)

file.close()