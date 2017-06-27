# -*- coding: utf-8 -*-

import pyshark

timestamp=0	
count=0
d=0
e=0


capture = pyshark.LiveCapture(interface='Wi-Fi',output_file='newpcap.pcapng')
#cap = pyshark.FileCapture('newpcap.pcapng', only_summaries=True)


# timestamp0=float(capture[0].sniff_timestamp)
# print 'Timestamp of first packet=%f' % (timestamp0)
length=0
capture.sniff(timeout=10)
print length

for pkt in capture:
	c=pkt.length
	d=c
	print d
	# e=c-d
	# print c
	# print e
	
	for pkt in capture:
	
		c=pkt.length
		pkt.length=long(pkt.length)+length
		length=float(pkt.length)
		count=count+1
		bandwidth=(length*100000000)/float(pkt.sniff_timestamp)
		print 'Count=%d Length=%d Bandwidth_percent= %f Protocol=%s TImestamp=%s' % (count,pkt.length,bandwidth,pkt.highest_layer,pkt.sniff_timestamp)
	
