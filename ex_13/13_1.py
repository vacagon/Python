import  xml.etree.ElementTree as ET

data = '''<person>
    <name>Gonzalo</name>
    <phone type = "int1">
        +34 648448874
    </phone>
    <email hide = "yes" />
</person>'''

tree = ET.fromstring(data) #tree is an object
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))
