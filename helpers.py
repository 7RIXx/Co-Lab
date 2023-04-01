#!/bin/env python3

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
	
