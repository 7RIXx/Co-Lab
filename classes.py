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
		
		# Label the location we will be monitoring
		# Using a .txt file with a few lines of foo for now to test the logic
		self.location = '/dev/net/' + args.interface
		
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
			
		return self.refined_harvest
	
		
			
		# Debug Test
		if args.debug:
			for item in self.raw_harvest:
				print('\r\n' + str(item))
