import docker
client = docker.APIClient(base_url='npipe:////./pipe/docker_engine')

if(client.containers(filters={'name':'second'})):
	client.stop(container='second')
	client.remove_container(container='second')
	
if(client.containers(filters={'name':'second_1'})):
	client.stop(container='second_1')
	client.remove_container(container='second_1')
	
if(client.containers(filters={'name':'second_2'})):
	client.stop(container='second')
	client.remove_container(container='second_2')
	
if(client.containers(filters={'name':'webfilter'})):
	client.stop(container='webfilter')
	client.remove_container(container='webfilter')
	
if(client.containers(filters={'name':'webfilter_1'})):
	client.stop(container='webfilter_1')
	client.remove_container(container='webfilter_1')
	
if(client.containers(filters={'name':'webfilter_2'})):
	client.stop(container='webfilter_2')
	client.remove_container(container='webfilter_2')
	

