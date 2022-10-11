import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = "AIzaSyBBG1Q5OyTMQc1p6eRycgh_N5MFp0gdDuA"

serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
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
    print(json.dumps(js, indent=4))
    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print(lat, lng)
    location = js["results"][0]['formatted_address']
    print(location)
