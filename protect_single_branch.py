#!/usr/bin/python

import requests

payload = { 'private_token' : 'rv1YLMiyJN45fAm37fFs'}


for index in range(1,200):
	
	r_str = "http://192.168.1.203/api/v3/projects/"+str(index)

	r = requests.get ( r_str , params=payload )

	print(r.url)
	print("r.status_code:",r.status_code)
	if (r.status_code == 404): continue
	#print(r.content)

	contents = r.content.replace("false","False")
	contents = contents.replace("true","True")
	contents = contents.replace("null","None")
	contents = eval(contents)
	print(contents['id'],contents['name_with_namespace'],len(contents))

	r_branches = requests.get(r_str + "/repository/branches", params=payload)
	print(r_branches.url)
	print(r_branches.status_code)
	#print("branches:" + r.text)

	
	if "release" in r_branches.text:
		r = requests.put(r_str + "/repository/branches/release/protect", params=payload)
		print(r.url)
		print(r.status_code)

	if "develop" in r_branches.text:
		develop_params = { 'private_token' : 'rv1YLMiyJN45fAm37fFs'}
		develop_params["developers_can_push"] = "true"
		develop_params["developers_can_merge"] = "true"
		r = requests.put(r_str + "/repository/branches/develop/protect", params=develop_params)
		print(r.url)
		print(r.status_code)





