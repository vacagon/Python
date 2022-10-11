import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_1649626.html'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

#List of all anchor tags
tags = soup('span')
num_list = list()
for tag in tags:
    st = str(tag)
    num = re.findall('([0-9].*)<',st)
    x = int(num[0])
    num_list.append(x)
print(sum(num_list))
