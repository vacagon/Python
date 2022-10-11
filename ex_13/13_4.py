import json


data = '''{
    "name" : "Gonzalo",
    "phone" : {
        "type" : "intl",
        "number" : "+34 648448874"
    },
    "email" : {
        "hide" : "yes"
    }
}'''


info = json.loads(data) # info is Python dictionary
print('Name: ', info["name"])
print('Hide: ', info["email"]["hide"])
