import re


patron = re.compile(r'\.')
text = 'Regular expresions y la oncha de tu madre me tenes los huevos como el 2 de oro 123456789 ./""-_ caca'

matches = patron.search(text)
for match in matches:
    print(match)
