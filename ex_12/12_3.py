import urllib.request, urllib.parse, urllib.error
import re
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
ddd = dict()
for line in fhand:
    line = line.decode().split()
    for word in line:
        if "l" in word:
            ddd[word] = ddd.get(word, 0) + 1

f = open("myfile.txt", 'w')
for k,v in ddd.items():
    newtup = (v,k)
    new_string = str(newtup)
    list_words.append(new_string)
list_words.sort(reverse=True)
for t in list_words:
    new_string = str(t)
    f.write(new_string + '\n')
