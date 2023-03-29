#!/bin/env python3

import argparse

help_menu = '''

	PLACEHOLDER FOR ASCII ART


	-h, --help :: Show this menu
	
	--debug :: Shows various developing cues used in production
	
	





'''







### ARGUMENT PARSER ###

# build argument parser
parser = argparse.ArgumentParser(add_help=False)

parser.add_argument('-h', '--help', action='store_true')
parser.add_argument('--debug', action='store_true')

# parse passed argumentation
args = parser.parse_args()

