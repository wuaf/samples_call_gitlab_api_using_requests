#!/usr/bin/python

import requests

payload = { 	'private_token' : 'vo1jP9en1TGrVDvTbS2o' }



r = requests.get ( "http://192.168.1.203/api/v3/groups" , params=payload )

print(r.url)
print(r.status_code)
print(r.content)
print(type(r.content))

contents = r.content.replace("false","False")
contents = contents.replace("true","True")
contents = contents.replace("null","None")

contents = eval(contents)

#print(len(contents))

for item in contents:
	print(item['id'],item['name'],len(item))





