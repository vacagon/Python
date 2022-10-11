import json


inpt = '''[
    {"id":"001",
     "x": "2",
     "name":"Gonzalo"
     },
    {"id":"009",
     "x":"7",
     "name":"Gonzalo"
    }
]'''

info = json.loads(inpt)
print('User count:', len(info))
for item in info:
    print('Name: ', item['name'])
    print('Id: ', item['id'])
    print('Attribute: ', item['x'])
