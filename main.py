#!/bin/env python3


### IMPORTS ###

from arguments import args
import classes as c
import helpers as h
import headers as hd
from time import sleep
#from sniffie import Sniffie
### END IMPORTS ###



### MAIN EXECUTION SEQUENCE ###

# Make it fancy
if not args.quick:
	print(hd.pretty_banner + '\n\n')
	


# Snoopie Class Call
if args.snoop:

	if not args.quick:
		print(' Harvesting data ... \n\n')

	snoopie = c.Snoopie()

	snoopie.harvest()
	
	if not args.quick:
		print('\n\n Analyzing data ... \n\n')

	snoopie.analyze()
	
	if not args.quick:
		print('\n\n Reporting suspicious listings ... \n\n')

	snoopie.report()

# End Snoopie Class Call

# Sniffie Class Call
elif args.sniff:

	packets = Sniffie()

	for packet in packets.capture_network_traffic():
		print(f'\n{packet}')
		
	'''
	
	NEED SNIFFIE EXECUTION SEQUENCE IN HERE
	
	'''
	
	
# End Sniffie Class Call

else:

	print(hd.help_menu)

### END MAIN EXECUTION SEQUENCE ###
