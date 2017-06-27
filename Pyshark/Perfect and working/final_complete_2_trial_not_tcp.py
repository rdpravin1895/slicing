# -*- coding: utf-8 -*-

import pyshark
import docker
import json
import ast
client = docker.APIClient(base_url='npipe:////./pipe/docker_engine')

timestamp=0	
pktcount_n=0
length=0
start=0
count_n=0
count_n1=0
count_n2=0
count_n3=0
mem=0


capture = pyshark.LiveCapture(interface='Wi-Fi',output_file='newpcap.pcapng')

capture.sniff(timeout=0.1)
#cap = pyshark.FileCapture('newpcap.pcapng', only_summaries=True)






#timestamp0=float(capture[0].sniff_timestamp)
#print 'Timestamp of first packet=%f' % (timestamp0)



for pkt in capture:

	pkt.length=long(pkt.length)#+length
	length=float(pkt.length)
	pktcount_n=pktcount_n+1
	bandwidth=int((length*100000000)/float(pkt.sniff_timestamp))
	
		
	print ' Length=%d Bandwidth_percent= %d Highest layer=%s ' % (pkt.length,bandwidth,pkt.highest_layer)
	if(pkt.highest_layer!='TCP'):
	
		if(start1==0):
			
			list=client.containers(all=True)
			ngn='nginx' in json.dumps(list)
			print ngn


			if(ngn==False):
				# client.stop(container='nginx')
				# client.remove_container(container='nginx')

				# client.stop(container='second')
				# client.remove_container(container='second')
		
				
				
				container=client.create_container('nginx',ports=[80],name='nginx',detach=True,host_config=client.create_host_config(port_bindings={80:('127.0.0.1',4003)}))
				client.containers()
				client.start(container='nginx')
				print 'nginx has been created'
			
			start1=start1+1
			
		if(bandwidth>50):
		
			count_n2=count_n2+1
			if(count_n2!=0 and count_n2%100==0):
			
				list=client.containers(all=True)
				ngn1='nginx_1' in json.dumps(list)

				
				if(ngn1==False):
					
					
					container=client.create_container('nginx',ports=[80],name='nginx_1',detach=True,host_config=client.create_host_config(port_bindings={80:('127.0.0.1',4004)}))
					client.containers()
					client.start(container='nginx_1')
					print 'nginx_1 has been added'
					count_n3=0
				
			if(count_n2<50):
				{
				}
			
		if(bandwidth>75):
		
			count_n=count_n+1
			if(count_n!=0 and count_n%100==0):
			
				list=client.containers(all=True)
				ngn2='nginx_2' in json.dumps(list)

				
				if(ngn2==False):
					
					
					container=client.create_container('nginx',ports=[80],name='nginx_2',detach=True,host_config=client.create_host_config(port_bindings={80:('127.0.0.1',4005)}))
					client.containers()
					client.start(container='nginx_2')
					print 'nginx_2 has been added'
					count_n1=0
				
			if(count_n<50):
				{
				}
				
		elif(bandwidth<75):
			
			if(count_n>=100):
				
				if(bandwidth<50 and bandwidth>0):
		
					if(count_n2>=100):
			
						count_n3=count_n3+1
						if(count_n3!=0 and count_n3%500==0):
					
							list=client.containers(all=True)
							ngn1='nginx_1' in json.dumps(list)

							
				
						if(ngn1==True):
							
							client.stop(container='nginx_1')
							client.remove_container(container='nginx_1')
							print 'nginx_1 has been removed'
							count_n3=0	
							count_n2=0		
			
				count_n1=count_n1+1
				if(count_n1!=0 and count_n1%500==0):
				
					list=client.containers(all=True)
					ngn2='nginx_2' in json.dumps(list)

					
				
					if(ngn2==True):	
						
						client.stop(container='nginx_2')
						client.remove_container(container='nginx_2')
						print 'nginx_2 has been removed'
						count_n1=0
						count_n=0
				
		print 'count_n=%d count_n1=%d count_n2=%d count_n3=%d' % (count_n,count_n1,count_n2,count_n3)	
		# statistics=client.stats(container='nginx',decode=True,stream=False)
		# proper=ast.literal_eval(json.dumps(statistics))
		# memory=float(proper['memory_stats']['usage'])
		# mem+=float(memory/(1024*1024))
		# print 'RAM=%f' %(mem) + 'Mb'