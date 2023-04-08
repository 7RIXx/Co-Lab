#!/bin/env python3

from arguments import args
import math

'''

Helper function to unpack the tuple of Snoopie Class connection harvest

'''

def transform_tuple(single_connection):
	
	# Cast name tuple into dictionary
	connection_dict = single_connection._asdict()
	
	# Create custom dictionary
	controlled_dict = {}
	
	# Move over important values
	controlled_dict['Local Host'] = connection_dict['laddr']
	controlled_dict['Remote Host'] = connection_dict['raddr']
	controlled_dict['Protocol'] = connection_dict['type']
	controlled_dict['Network'] = connection_dict['family']
	controlled_dict['ProcessID'] = connection_dict['pid']
	
	# Transform the values
	# Transform Local Host value
	try:
		controlled_dict['Local Host'] = str(connection_dict['laddr']).split('\'', 2)[1]
	except IndexError:
		controlled_dict['Local Host'] = None
	

	# Transform Remote Host value
	try:
		controlled_dict['Remote Host'] = str(connection_dict['raddr']).split('\'', 2)[1]
	except IndexError:
		controlled_dict['Remote Host'] = None
	

	# Transform Protocol value
	if str(connection_dict['type']) == 'SocketKind.SOCK_STREAM':
		controlled_dict['Protocol'] = 'TCP'
		
	elif str(connection_dict['type']) == 'SocketKind.SOCK_DGRAM':
		controlled_dict['Protocol'] = 'UDP'
		
	else:
		controlled_dict['Protocol'] = 'Unknown'
	

	# Transform Network value
	if str(connection_dict['family']) == 'AddressFamily.AF_INET':
		controlled_dict['Network'] = 'IPv4'
		
	elif str(connection_dict['family']) == 'AddressFamily.AF_INET6':
		controlled_dict['Network'] = 'IPv6'
		
	else:
		controlled_dict['Network'] = 'Unknown'
		
	
	# Transform PID value
	controlled_dict['ProcessID'] = str(connection_dict['pid'])
	
	
	
	return controlled_dict
	
	

'''

Helper function to help parse_proc display appropriate data;
	Goes inside parse_proc, which then goes inside get_data
	
'''

def convert_bytes(number_in_bytes):
# Takes the raw bytes data and converts it to an appropriate format based on its size
# Converts to an int because we are passing it the string of a number from outside ;; convert back at end to add the notation
	
	num, value = int(number_in_bytes), 0
	terabytes, gigabytes, megabytes, kilobytes = 1099511627776, 1073741824, 1048576, 1024
	tera, giga, mega, kilo = False, False, False, False
	
	
	# if > 1099511627776 then TB	
	if num >= terabytes:
		tera = True

	# if > 1073741824 then GB
	elif num >= gigabytes:
		giga = True
	
	# if > 1048576 then MB
	elif num >= megabytes:
		mega = True
	
	# if > 1024 then KB
	elif num >= kilobytes:
		kilo = True

	if tera:
		value = math.ceil(num / terabytes)
		return str(value) + ' TB'
	elif giga:
		value = math.ceil(num / gigbytes)
		return str(value) + ' GB'
	elif mega:
		value = math.ceil(num / megabytes)
		return str(value) + ' MB'
	elif kilo:
		value = math.ceil(num / kilobytes)
		return str(value) + ' KB'
	else:
		value = math.ceil(num)
		return str(num) + ' B'
	
	
	
'''

Helper function to help the get_data function parse for Linux;
	Goes inside get_data

'''
	
def parse_proc(chunk):

	# Eliminate column headers
	# Creates a MULTI-LINE STRING of all interface readouts
	chunk = chunk[199:]
	
	# Seperate into a list organized by interface
	# Creates a LIST of interface readouts
	chunk = chunk.split('\n')
	
	#debug
	print('\n' + 'CHUNK' + '\n' + str(chunk) + '\n')
	
	# Crush all the whitespace
	for char in range(len(chunk)):
		chunk[char] = chunk[char].replace('    ',' ').replace('  ',' ').replace('  ',' ').lstrip()
		
	# Remove relics remaining in object
	chunk.remove('')
	chunk.remove('')
	
	# Create placeholders to sum into
	# Collects the sum across all interfaces by PID
	up, down = 0,0
	
	# Loop through the list of interfaces and pull the appropriate columns
	# They are pulled as strings so need int conversion to do the addition
	for interface in chunk:
		up += int(interface.split(":")[1].lstrip().split(" ")[0])
		down += int(interface.split(":")[1].lstrip().split(" ")[8])
	
	# Now we need to take the total sum, convert it by size and flip it back to a string
	# String required so we can add the appropriate notation (KB/MB etc..)
	# Convert bytes can take int or str but returns a str
	up = convert_bytes(up)
	down = convert_bytes(down)
	
	if args.debug:
		print(f'\nUp: {up}\nDown: {down}\n') 
	
	updown = [up,down]
	
	# Return a LIST with up and down
	return updown

	
'''

Helper function to scrape up/down data from system and parse it to be passed into the ListDict

'''

def get_data(single_connection,pid_as_str):
	
	return_data = []
	
	#for listing in listDict:
		# Scrape up/down data in the case the conn has active PID
		# Check if PID is a number or resolves to None
		
	pid = pid_as_str
		
	try: 
	

		# PID file location to pull up/down data from
		location = str('/proc/' + pid + '/net/dev')
		f = open(location,'r')
			
		#debug
		print('\ntest file open\n')
		
		proc_dev_net_return = f.read()
			
		# Parse the file to get the numbers	
		return_data = parse_proc(proc_dev_net_return)

			
	
	except:
		# If process does not resolve to an int then skip
		if args.debug:
			print('Skipped One')
		raise
		
	# Returns the two element LIST from parse_proc
	return return_data	
	
	
	
	
	
	
if __name__ == "__main__":

	sample = '''Inter-|   Receive                                                |  Transmit
 face |bytes    packets errs drop fifo frame compressed multicast|bytes    packets errs drop fifo colls carrier compressed
    lo:   74833     680    0    0    0     0          0         0    74833     680    0    0    0     0       0          0
enp4s0:       0       0    0    0    0     0          0         0        0       0    0    0    0     0       0          0
wlp5s0: 129105035   88014    0    0    0     0          0         0  4531208   39727    0    0    0     0       0          0
lxcbr0:       0       0    0    0    0     0          0         0        0       0    0    0    0     0       0          0
'''
	
	
	get_data(sample,'2190')
	
	
	
	
	
	
	
	
	
	
	
	
	
