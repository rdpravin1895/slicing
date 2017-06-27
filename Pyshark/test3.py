# -*- coding: utf-8 -*-

import pyshark
import docker
client = docker.APIClient(base_url='npipe:////./pipe/docker_engine')

timestamp=0	
count=0
length=0
start=0

capture = pyshark.LiveCapture(interface='Wi-Fi',output_file='newpcap.pcapng')
#cap = pyshark.FileCapture('newpcap.pcapng', only_summaries=True)

capture.sniff(timeout=10)

timestamp0=float(capture[0].sniff_timestamp)
print 'Timestamp of first packet=%f' % (timestamp0)



for pkt in capture:

	
	pkt.length=long(pkt.length)#+length
	length=float(pkt.length)
	count=count+1
	bandwidth=(length*100000000)/float(pkt.sniff_timestamp)
	print 'Count=%d Timestamp=%s Length=%d Bandwidth_percent= %f Highest layer=%s Transport layer= %s' % (count,pkt.sniff_timestamp,pkt.length,bandwidth,pkt.highest_layer,pkt.transport_layer)
	if(pkt.highest_layer=='QUIC'):
	
		if(start==0):
		
			response=[line for line in client.build(path="C:\Users\pravin\Desktop\docker\docker1",tag="trial/1")]
			client.images()
			container=client.create_container('trial/1',ports=[80],name='second',detach=True,host_config=client.create_host_config(port_bindings={80:('127.0.0.1',6000)},mem_limit='1g',cpu_shares=60,cpuset_cpus='1'))
			client.containers()
			client.start(container='second')
			print 'Container 1 has been created for the first time'
			
			
			container=client.create_container('diladele/websafety',ports=[80,3128],name='webfilter',detach=True,host_config=client.create_host_config(port_bindings={80:('127.0.0.1',6003),3128:('127.0.0.1',3128)}))
			client.containers()
			client.start(container='webfilter')
			print 'Webfilter has been created'
			start=start+1
	
	