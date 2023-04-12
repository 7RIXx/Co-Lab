#!/bin/env python3

from arguments import args
import helpers as help
from netaddr import IPAddress
import pyshark, psutil, socket


'''

Classes for Traffic Monitor

'''


class Snoopie():
# Monitor network traffic historically, and if user says then save into a hidden file @ PWD
# Analyze the data harvested for malicious signs
	
	def __init__(self):

		# Temporary storehouse for initial incoming data
		self.raw_harvest = []
		
		# Refine and take control of the data
		self.refined_harvest = []
		
		# List suspicious connections
		self.suspect = []
		
		
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
			
			# Make code more readable
			conn = self.refined_harvest[connection]
			
			# Protect from dead connections
			if conn['ProcessID'] != 'None':
				
				# Take the two element LIST returned from get_data
				# And insert 'DataUp' 'DataDown' elements to the refined_harvest DICT
				values = help.get_data(conn,conn['ProcessID'])
				conn['UpData'] = values[0]
				conn['DownData'] = values[1]			
			
		return self.refined_harvest
	
		
			
		# Debug Test
		if args.debug:
			for item in range(len(self.raw_harvest)):
				print(str(item) + ': \n' + 'RAW: \n' + str(self.raw_harvest[item]))
			for item in self.refined_harvest:
				print(str(item) + ': \n' + 'REFINED: \n' + str(self.refined_harvest[item]))
			
			
	# Create a method to analyze the refined_harvest (dns_check, size_check, secure_check)
	def analyze(self):
	
		# Make code more readable
		harvest = self.refined_harvest
		
		# for each connection, check if the IP resolves via DNS
		for item in range(len(harvest)):
			
			# Make code more readable
			remip = harvest[item]['Remote Host']
			
			try:
				if args.debug:
					print(remip)
				
				# Try a reverse DNS lookup
				dnsname = socket.gethostbyaddr(remip)[0]
				
				# Add Host Name to dict
				harvest[item]['Host Name'] = dnsname
				
				#db
				print(f'POSTRES: {dnsname}')
			
			# If the lookup fails and the IP isn't 'None' then call it suspect
			except:
				if args.debug:
					raise
				
				# Check that there was an IP to check in on
				if remip != 'None':
				
					# Copy dict object
					sus_dict = harvest[item]
					
					# Add reason for suspicion 
					sus_dict['Suspicion'] = 'DNS does not resolve'
					
					# Pass into a seperate list for later assessment
					self.suspect.append(sus_dict)
						
				
				# Proceed to the next assessment
				continue
			
		# for each connection, check if it was connected via HTTPS
		for item in range(len(harvest)):
		
			# Make code more readable
			rempo = harvest[item]['Remote Port']
		
			if rempo != '443':
				
				# Check there was a port to check in on
				if rempo != 'None':
					
					# Copy dict object
					sus_dict = harvest[item]
					
					# Add reason for suspicion
					sus_dict['Suspicion'] = 'HTTPS not present'
					
					# Pass into a seperate list for later assessment
					self.suspect.append(sus_dict)
					
		# for each connection, check if there is a suspicious up or down data transfer
		for item in range(len(harvest)):
			
			# Check that we have a connection with valid data to assess
			if harvest[item]['ProcessID'] != 'None':			
					
				# Make code more readable
				dataup = harvest[item]['UpData']
				datadown = harvest[item]['DownData']
			
				# Check if the connection is taking significantly more data than it's giving
				# We want to convert both numbers from their KB/MB form and turn back to bytes
				# Then we do upload_bytes divided by download_bytes
				# This will give us a 1:N ratio
				# Then we assess to determine if the up is too many times more than the down	
			
				# Check that there is data to read
				if 'None' not in [dataup,datadown]:
			
					# Run through helper func to get individual bytes back
					# Send strings into little_bytes but receive back ints
					[upbytes,downbytes] = help.little_bytes(dataup,datadown)
			
					# Calculate the 1:N raio
					metric = int(upbytes) // int(downbytes)
			
					# If the ratio is 150 percent or more then classify as suspicious
					if metric >= 2:
				
						#db
						print(f' METRIC: {metric}')
					
						# Call suspect
						# Copy dict object
						sus_dict = harvest[item]
						
						# Add reason for suspicion
						sus_dict['Suspicion'] = 'Sending significantly more data than receiving'
					
						# Pass into a seperate list for later assessment
						self.suspect.append(sus_dict)				
				
		
		
		# Finally consolidate all suspect connections
		# If the same connection is suspect for multiple reasons, each reason lists the entire connection again
		# So we will find such cases and make them into a single connection listing with multiple reasons under 'Suspicion'
		help.sus_check(self.suspect)		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
