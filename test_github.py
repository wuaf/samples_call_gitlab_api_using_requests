#!/usr/bin/python

import requests

payload = { 'private_token' : 'vo1jP9en1TGrVDvTbS2o' }


'''
payload["name"] = "test_http"
payload["path"] = "test_http_path"

r = requests.post ( "http://192.168.1.203/api/v3/groups" , params=payload )

print(r.status_code)
print(r.text)


r = requests.get ( "http://192.168.1.203/api/v3/groups/lib/projects" , params=payload )

print(r.url)
print(r.status_code)
print(r.content)
print(type(r.content))

content = list(r.content)
for kv in content:
    print(kv)

print(type(r.json()[0]))
print(eval(r.content))[0])
'''

#for each project, add protect on branch release and master
'''
pr = requests.get( "http://192.168.1.203/api/v3/projects/109", params = payload)

content = pr.content.replace("false","False")
content = content.replace("true","True")
content = content.replace("null","None")
print(type(content))
print(len(content))
pm = eval(content)
print(len(pm))
#print(type(pm))
#print(pm[0])
#print(pm[0].keys())
#print(pm[0]['id'],pm[0]['namespace'],pm[0]['name'])

project = pm
print(project['id'],project['name'],project['namespace'])
#for project in pm:
#    print(project['id'],project['name'],project['namespace'])
'''

for index in range(1,200):
	pr = requests.get( "http://192.168.1.203/api/v3/projects/"+str(index), params = payload)
	content = pr.content.replace("false","False")
        content = content.replace("true","True")
        content = content.replace("null","None")
        pm = eval(content)
	print(pm)    
 	pm.    
	id = pm['id']
        name = pm['name']
        print(id, name)




 



