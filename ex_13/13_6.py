import json
import urllib.request, urllib.parse, urllib.error

url = 'http://py4e-data.dr-chuck.net/comments_1649629.json'
uh = urllib.request.urlopen(url)
data = uh.read().decode()
info = json.loads(data)
comments = info['comments']
s = 0
for item in comments:
    n = int(item['count'])
    s = s + n
print(s)
