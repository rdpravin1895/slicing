# -*- coding: utf-8 -*-

import pyshark
import docker
import json
import ast
client = docker.APIClient(base_url='npipe:////./pipe/docker_engine')

timestamp=0	
pktcount=0
length=0
start=0
count=0
count1=0
count2=0
count3=0

capture = pyshark.LiveCapture(interface='Wi-Fi',output_file='newpcap.pcapng')
#cap = pyshark.FileCapture('newpcap.pcapng', only_summaries=True)


capture.sniff(timeout=10)

timestamp0=float(capture[0].sniff_timestamp)
print 'Timestamp of first packet=%f' % (timestamp0)



for pkt in capture:

	
	pkt.length=long(pkt.length)#+length
	length=float(pkt.length)
	pktcount=pktcount+1
	bandwidth=(length*100000000)/float(pkt.sniff_timestamp)
	
		
	print ' Length=%d Bandwidth_percent= %f Highest layer=%s ' % (pkt.length,bandwidth,pkt.highest_layer)
	if(pkt.highest_layer=='TCP'):
	
		if(start==0):
		
			list=client.containers()
			wf='webfilter' in json.dumps(list)
			print wf

			sc='second' in json.dumps(list)
			print sc

			if(wf==True and sc==True):
				client.stop(container='webfilter')
				client.remove_container(container='webfilter')

				client.stop(container='second')
				client.remove_container(container='second')
		
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
			
		if(bandwidth>50):
		
			count2=count2+1
			if(count2==50):
			
				container=client.create_container('trial/1',ports=[80],name='second_1',detach=True,host_config=client.create_host_config(port_bindings={80:('127.0.0.1',8000)},mem_limit='1g',cpu_shares=60,cpuset_cpus='1'))
				client.containers()
				client.start(container='second_1')
				print 'Second_1 has been added'
				
				container=client.create_container('diladele/websafety',ports=[80,3128],name='webfilter_1',detach=True,host_config=client.create_host_config(port_bindings={80:('127.0.0.1',8003),3128:('127.0.0.1',5128)}))
				client.containers()
				client.start(container='webfilter_1')
				print 'Webfilter_1 has been added'
				
			if(count2<50):
				{
				}
			
			if(bandwidth>75):
			
				count=count+1
				if(count==50):
				
					container=client.create_container('trial/1',ports=[80],name='second_2',detach=True,host_config=client.create_host_config(port_bindings={80:('127.0.0.1',7000)},mem_limit='1g',cpu_shares=60,cpuset_cpus='1'))
					client.containers()
					client.start(container='second_2')
					print 'Second_2 has been added'
					
					container=client.create_container('diladele/websafety',ports=[80,3128],name='webfilter_2',detach=True,host_config=client.create_host_config(port_bindings={80:('127.0.0.1',7003),3128:('127.0.0.1',4128)}))
					client.containers()
					client.start(container='webfilter_2')
					print 'Webfilter_2 has been added'
					
				if(count<50):
					{
					}
				
			elif(bandwidth<75):
				
				if(count>=50):
				
					count1=count1+1
					if(count1==300):
					
						client.stop(container='second_2')
						client.remove_container(container='second_2')
						print 'Second_2 has been removed'
						client.stop(container='webfilter_2')
						client.remove_container(container='webfilter_2')
						print 'Webfilter_2 has been removed'
						count1=0
						count=0
				
				
		elif (bandwidth<50 and bandwidth>0):
			
			if(count>=50):
				
				count1=count1+1
				if(count1==300):
				
					client.stop(container='second_2')
					client.remove_container(container='second_2')
					print 'Second_2 has been removed'
					client.stop(container='webfilter_2')
					client.remove_container(container='webfilter_2')
					print 'Webfilter_2 has been removed'
					count1=0
		
			if(count2>=50):
			
				count3=count3+1
				if(count3==300):
				
					client.stop(container='second_1')
					client.remove_container(container='second_1')
					print 'Second_1 has been removed'
					client.stop(container='webfilter_1')
					client.remove_container(container='webfilter_1')
					print 'Webfilter_1 has been removed'
					count3=0	
					count2=0
		print 'Count=%d Count1=%d Count2=%d Count3=%d' % (count,count1,count2,count3)		
	
	