#!/bin/env python3


### IMPORTS ###

from arguments import args
import classes as c
from sniffie import Sniffie
### END IMPORTS ###




### Production Testing ###

# Test Snoopie Class
snoopie = c.Snoopie()
for item in snoopie.harvest():
	print('\n\n')
	print(item)


packets = Sniffie()

for packet in packets.capture_network_traffic():
	print(f'\n{packet}')


### END PRODUCTION TESTING ###
