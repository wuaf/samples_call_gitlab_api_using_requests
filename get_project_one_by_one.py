#!/usr/bin/python

import requests

payload = { 	'private_token' : 'vo1jP9en1TGrVDvTbS2o'}


for index in range(1,200):
	r = requests.get ( "http://192.168.1.203/api/v3/projects/"+str(index) , params=payload )

	print(r.url)
	print("r.status_code:",r.status_code)
	if (r.status_code == 404): continue
	print(len(r.content))
	print(type(r.content))

	contents = r.content.replace("false","False")
	contents = contents.replace("true","True")
	contents = contents.replace("null","None")

	contents = eval(contents)

	#print(len(contents))

	item = contents
	print(item['id'],item['name_with_namespace'],len(item))





