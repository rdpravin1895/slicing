# -*- coding: utf-8 -*-

import pyshark

timestamp=0	
count=0
length=0

capture = pyshark.LiveCapture(interface='Wi-Fi',output_file='newpcap.pcapng')
#cap = pyshark.FileCapture('newpcap.pcapng', only_summaries=True)
capture.sniff(timeout=10)


# timestamp0=float(capture[0].sniff_timestamp)
# print 'Timestamp of first packet=%f' % (timestamp0)



for pkt in capture:

	
	pkt.length=long(pkt.length)#+length
	length=float(pkt.length)
	count=count+1
	bandwidth=(length*100000000)/float(pkt.sniff_timestamp)
	print 'Count=%d Timestamp=%s Length=%d Bandwidth_percent= %f Protocol=%s' % (count,pkt.sniff_timestamp,pkt.length,bandwidth,pkt.highest_layer)
	
	