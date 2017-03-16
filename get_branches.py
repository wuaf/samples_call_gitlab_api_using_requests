#!/usr/bin/python

import requests

payload = { 'private_token' : 'rv1YLMiyJN45fAm37fFs'}

r = requests.get("http://192.168.1.203/api/v3/projects/")

print(r.url)
print(r.status_code)
print(r.text)
'''
for index in range(8,9):
	
	r = requests.get ( "http://192.168.1.203/api/v3/projects/"+str(index) , params=payload )

	print(r.url)
	print("r.status_code:",r.status_code)
	if (r.status_code == 404): continue
	print(r.content)

	contents = r.content.replace("false","False")
	contents = contents.replace("true","True")
	contents = contents.replace("null","None")
	contents = eval(contents)
	print(contents['id'],contents['name_with_namespace'],len(contents))

	r = requests.get("http://192.168.1.203/api/v3/projects/" + str(index)+ "/repository/branches")
	print(r.url)
	print("branches:" + r.text)

	
	if "release" in r.text:
		r = requests.put("http://192.168.1.203/api/v3/projects/" + str(index)+ "/repository/branches/release/protect")
		print(r.url)
		print(r.text)

'''


