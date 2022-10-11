import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_1649628.xml'
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
data = data.decode()
tree = ET.fromstring(data)
results = tree.findall('comments/comment')
suma = 0
for item in results:
    st = item.find('count').text
    suma = suma + int(st)
print(suma)
