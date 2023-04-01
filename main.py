#!/bin/env python3


### IMPORTS ###

from arguments import args
import classes as c

### END IMPORTS ###




### Production Testing ###

# Test Snoopie Class
snoopie = c.Snoopie()
for item in snoopie.harvest():
	print('\n\n')
	print(item)


### END PRODUCTION TESTING ###
