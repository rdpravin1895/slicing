import docker 
import json,ast
client = docker.APIClient(base_url='npipe:////./pipe/docker_engine')

list=client.containers()
# print type(list)
# c='Status' in list
# print c
#print json.dumps(list)
wf='webfilter' in json.dumps(list)
print wf
# proper=ast.literal_eval(json.dumps(list))
# print proper