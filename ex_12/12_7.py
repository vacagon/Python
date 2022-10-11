import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re


def find_url(url_html, pos):
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    html = urllib.request.urlopen(url_html, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    urls = list()
    for tag in tags:
        st = str(tag)
        url = re.findall('href="(.*)"', st)
        if len(url) != 1:
            continue
        urls.append(url[0])
    r = str(urls[pos - 1])
    return r


root_url = list()
root_url.append('http://py4e-data.dr-chuck.net/known_by_Strachan.html')

position = 18
count = 7
i = 0
while i <= count:
    new_url = str(root_url[i])
    root_url.append(find_url(new_url, position))
    name = re.findall('http://py4e-data.dr-chuck.net/known_by_(\w*)\.', root_url[i])
    i = i+1

print(name)
