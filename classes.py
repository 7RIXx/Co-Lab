#!/bin/env python3

from arguments import args
import helpers as help
from netaddr import IPAddress
import pyshark, psutil

'''

Classes for Traffic Monitor

'''


class Snoopie():
# Monitor network traffic and copy IPs, Frequency, and DataSize into a hidden file @ PWD
	
	def __init__(self):
		# Create dict to hold data, this dict will be output into other classes
		self.doghouse = {}
		
		
		# Temporary storehouse for initial incoming data
		self.raw_harvest = []
		
		# Refine and take control of the data
		self.refined_harvest = []
		
		
	# Create method to bring data in from location
	def harvest(self):
		# get all active net connections returned in a list of named tuples
		# includes addressFamily, tcp/udp, local_addr, remote_addr, conn_status, process_id
		self.raw_harvest = psutil.net_connections()
		
		# Unpack the tuple, take control of data, and customize output
		for connection in self.raw_harvest:
			self.refined_harvest.append(help.transform_tuple(connection))
			
		# For active PIDs, locate the total Up/Down bytes and append to each connection-set
		# Can access on Linux at /proc/[PID]/net/dev
		for connection in range(len(self.refined_harvest)):
			
			# Make following codeblock more readable
			tmp = self.refined_harvest[connection]
			
			# Protect from dead connections
			if tmp['ProcessID'] != 'None':
				
				# Take the two element LIST returned from get_data
				# And insert 'DataUp' 'DataDown' elements to the refined_harvest DICT
				values = help.get_data(tmp,tmp['ProcessID'])
				tmp['UpData'] = values[0]
				tmp['DownData'] = values[1]
				
				
				
			
		return self.refined_harvest
	
		
			
		# Debug Test
		if args.debug:
			for item in self.raw_harvest:
				print('\r\n' + str(item))
			
