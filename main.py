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




test = Sniffie()
print(test.is_dns_resolvable())
print(test.is_ip_private())


### END PRODUCTION TESTING ###
