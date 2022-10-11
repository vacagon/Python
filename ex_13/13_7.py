import urllib.request, urllib.parse, urllib.error
import json
import ssl


serviceurl = 'http://py4e-data.dr-chuck.net/json?'
api_key = "42"
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter address: ')
    if len(address) < 1:
        break
    parms = dict()
    parms['address'] = address
    parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('Failure to Retrieve')
        print(data)
        continue
    oh =  open('json_data.json', 'w')
    oh.write(json.dumps(js, indent=1))
    place_id = js['results'][0]['place_id']
    print(place_id)
