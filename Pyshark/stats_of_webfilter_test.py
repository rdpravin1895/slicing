import docker
import json,ast
client = docker.APIClient(base_url='npipe:////./pipe/docker_engine')

statistics=client.stats(container='webfilter',decode=True,stream=False)
#print statistics

i=1;
while(i>0):
	proper=ast.literal_eval(json.dumps(statistics))
	memory=float(proper['memory_stats']['usage'])
	cpu=proper['cpu_stats']['system_cpu_usage']
	total_cpu=proper['cpu_stats']['cpu_usage']['total_usage']
	#print cpu
	#print total_cpu
	#cpupercent=cpu/total_cpu
	#print cpupercent
	#print memory
	mem=float(memory/(1024*1024))
	print 'RAM=%f' %(mem) + 'Mb'
	#print type(mem)
	#print proper
	i+=1

# cpu=dict((k, proper[k]) for k in ('name'))
# c='cpu_stats' in proper
# d='name' in proper
# e='system_cpu_usage' in proper

# proper = json.dumps(proper)
# loaded_r = json.loads(proper)
# print loaded_r['cpu_stats']

# proper1=ast.literal_eval(json.dumps(loaded_r))
# proper1=json.dumps(proper1)
# loaded_r1 = json.loads(proper1)
# print loaded_r1


# print c
# print d
# print e

