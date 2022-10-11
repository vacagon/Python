import re

p = '<p>Please click <a href="http://www.dr-chuck.com">here</a></p>'
url = re.findall('href="(.+)"',p)
print(url)
