#!/bin/env python3

from arguments import args

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
		self.location = 'testfile.txt'
		
		# Temporary storehouse for incoming data
		self.harLis = []
		
	# Create method to bring data in from location
	def harvest(self):
		with open(self.location, 'r+') as f:
		
			# Read each line into the temporary working file
			# Strip the newline char
			self.harLis = [x.strip() for x in f.readlines()]
			
			# Reset pointer
			f.seek(0)
			
		# Debug Test
		if args.debug:
			print(f'\n {self.harLis} \n')
