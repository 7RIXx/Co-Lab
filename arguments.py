#!/bin/env python3



help_menu = '''

	PLACEHOLDER FOR ASCII ART


	-h, --help :: Show this menu
	
	





'''







### ARGUMENT PARSER ###

# build argument parser
parser = argparse.ArgumentParser(add_help=False)

parser.add_argument('-h', '--help', action='store_true')


# parse passed argumentation
args = parser.parse_args()
