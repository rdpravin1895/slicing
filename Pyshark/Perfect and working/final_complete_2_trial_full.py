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
start1=0

count=0
count_n=0

count1=0
count_n1=0

count2=0
count_n2=0

count3=0
count_n3=0

mem=0


capture = pyshark.LiveCapture(interface='Wi-Fi',output_file='newpcap.pcapng')

capture.sniff(timeout=10)
#cap = pyshark.FileCapture('newpcap.pcapng', only_summaries=True)






#timestamp0=float(capture[0].sniff_timestamp)
#print 'Timestamp of first packet=%f' % (timestamp0)



for pkt in capture:

	pkt.length=long(pkt.length)#+length
	length=float(pkt.length)
	pktcount=pktcount+1
	bandwidth=int((length*100000000)/float(pkt.sniff_timestamp))
	
		
	print ' Length=%d Bandwidth_percent= %d Highest layer=%s ' % (pkt.length,bandwidth,pkt.highest_layer)
	if(pkt.highest_layer=='TCP'):
	
	#if the received packet is TCP
	
		if(start==0):
			
			list=client.containers(all=True)
			wf='webfilter' in json.dumps(list)
			print wf

			sc='testing' in json.dumps(list)
			print sc

			if(wf==False and sc==False):
				# client.stop(container='webfilter')
				# client.remove_container(container='webfilter')

				# client.stop(container='testing')
				# client.remove_container(container='testing')
		
				response=[line for line in client.build(path="C:\Users\pravin\Desktop\docker\docker1",tag="trial/1")]
				client.images()
				container=client.create_container('trial/1',ports=[80],name='testing',detach=True,host_config=client.create_host_config(port_bindings={80:('127.0.0.1',6000)},mem_limit='1g',cpu_shares=60,cpuset_cpus='1'))
				client.containers()
				client.start(container='testing')
				print 'Container 1 has been created for the first time'
				
				
				container=client.create_container('diladele/websafety',ports=[80,3128],name='webfilter',detach=True,host_config=client.create_host_config(port_bindings={80:('127.0.0.1',6003),3128:('127.0.0.1',3128)}))
				client.containers()
				client.start(container='webfilter')
				print 'Webfilter has been created'
			
			start=start+1
			
		if(bandwidth>50):
		
			count2=count2+1
			if(count2!=0 and count2%100==0):
			
				list=client.containers(all=True)
				wf1='webfilter_1' in json.dumps(list)

				sc1='testing_1' in json.dumps(list)
				
				if(wf1==False and sc1==False):
					container=client.create_container('trial/1',ports=[80],name='testing_1',detach=True,host_config=client.create_host_config(port_bindings={80:('127.0.0.1',8000)},mem_limit='1g',cpu_shares=60,cpuset_cpus='1'))
					client.containers()
					client.start(container='testing_1')
					print 'testing_1 has been added'
					
					container=client.create_container('diladele/websafety',ports=[80,3128],name='webfilter_1',detach=True,host_config=client.create_host_config(port_bindings={80:('127.0.0.1',8003),3128:('127.0.0.1',5128)}))
					client.containers()
					client.start(container='webfilter_1')
					print 'Webfilter_1 has been added'
					count3=0
				
			if(count2<50):
				{
				}
			
		if(bandwidth>75):
		
			count=count+1
			if(count!=0 and count%100==0):
			
				list=client.containers(all=True)
				wf2='webfilter_2' in json.dumps(list)

				sc2='testing_2' in json.dumps(list)
				
				if(wf2==False and sc2==False):
					container=client.create_container('trial/1',ports=[80],name='testing_2',detach=True,host_config=client.create_host_config(port_bindings={80:('127.0.0.1',7000)},mem_limit='1g',cpu_shares=60,cpuset_cpus='1'))
					client.containers()
					client.start(container='testing_2')
					print 'testing_2 has been added'
					
					container=client.create_container('diladele/websafety',ports=[80,3128],name='webfilter_2',detach=True,host_config=client.create_host_config(port_bindings={80:('127.0.0.1',7003),3128:('127.0.0.1',4128)}))
					client.containers()
					client.start(container='webfilter_2')
					print 'Webfilter_2 has been added'
					count1=0
				
			if(count<50):
				{
				}
				
		if(bandwidth<75):
			
			if(count>=100):
				
				if(bandwidth<50 and bandwidth>0):
		
					if(count2>=100):
			
						count3=count3+1
						if(count3!=0 and count3%500==0):
					
							list=client.containers(all=True)
							wf1='webfilter_1' in json.dumps(list)

							sc1='testing_1' in json.dumps(list)
				
						if(wf1==True and sc1==True):
							client.stop(container='testing_1')
							client.remove_container(container='testing_1')
							print 'testing_1 has been removed'
							client.stop(container='webfilter_1')
							client.remove_container(container='webfilter_1')
							print 'Webfilter_1 has been removed'
							count3=0	
							count2=0		
			
				count1=count1+1
				if(count1!=0 and count1%500==0):
				
					list=client.containers(all=True)
					wf2='webfilter_2' in json.dumps(list)

					sc2='testing_2' in json.dumps(list)
				
					if(wf2==True and sc2==True):	
						client.stop(container='testing_2')
						client.remove_container(container='testing_2')
						print 'testing_2 has been removed'
						client.stop(container='webfilter_2')
						client.remove_container(container='webfilter_2')
						print 'Webfilter_2 has been removed'
						count1=0
						count=0
				
		print 'Count=%d Count1=%d Count2=%d Count3=%d' % (count,count1,count2,count3)	
		# statistics=client.stats(container='webfilter',decode=True,stream=False)
		# proper=ast.literal_eval(json.dumps(statistics))
		# memory=float(proper['memory_stats']['usage'])
		# mem+=float(memory/(1024*1024))
		# print 'RAM=%f' %(mem) + 'Mb'
		
		count_n1=count_n1+1
		if(count_n1!=0 and count_n1%200==0):
		
			list=client.containers(all=True)
			ngn2='nginx_2' in json.dumps(list)

		
			if(ngn2==True):	
				client.stop(container='nginx_2')
				client.remove_container(container='nginx_2')
				print 'nginx_2 has been removed'
				count_n1=0
				count_n=0
			
		count_n3=count_n3+1
		if(count_n3!=0 and count_n3%200==0):
		
		
			list=client.containers(all=True)
			ngn1='nginx_1' in json.dumps(list)
		
			if(ngn1==True):
				client.stop(container='nginx_1')
				client.remove_container(container='nginx_1')
				print 'nginx_1 has been removed'
				count_n3=0	
				count_n2=0	
		
		print 'count_n=%d count_n1=%d count_n2=%d count_n3=%d' % (count_n,count_n1,count_n2,count_n3)
		print ''
	
	if(pkt.highest_layer!='TCP'):
	
	#if the received packet is not TCP
	
		if(start1==0):
			
			list=client.containers(all=True)
			ngn='nginx' in json.dumps(list)
			print ngn


			if(ngn==False):
				
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
				
		if(bandwidth<75):
			
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

		
		count1=count1+1
		if(count1!=0 and count1%200==0):
		
			list=client.containers(all=True)
			wf2='webfilter_2' in json.dumps(list)

			sc2='testing_2' in json.dumps(list)
		
			if(wf2==True and sc2==True):	
				client.stop(container='testing_2')
				client.remove_container(container='testing_2')
				print 'testing_2 has been removed'
				client.stop(container='webfilter_2')
				client.remove_container(container='webfilter_2')
				print 'Webfilter_2 has been removed'
				count1=0
				count=0
			
		count3=count3+1
		if(count3!=0 and count3%200==0):
		
		
			list=client.containers(all=True)
			wf1='webfilter_1' in json.dumps(list)

			sc1='testing_1' in json.dumps(list)
		
			if(wf1==True and sc1==True):
				client.stop(container='testing_1')
				client.remove_container(container='testing_1')
				print 'testing_1 has been removed'
				client.stop(container='webfilter_1')
				client.remove_container(container='webfilter_1')
				print 'Webfilter_1 has been removed'
				count3=0	
				count2=0	
		
		
		print 'Count=%d Count1=%d Count2=%d Count3=%d' % (count,count1,count2,count3)
		print ''