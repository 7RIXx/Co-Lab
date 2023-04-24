#!/bin/env python3

import argparse, psutil, os

help_menu = '''

	PLACEHOLDER FOR ASCII ART

	
	-to, --timeout :: Set a timeout delay (Range 1-1000)

	-i, --interface :: Set a network interface card
	
	-h, --help :: Show this menu
	
	--debug :: Shows various developing cues used in production
	
	





'''





### ARGUMENT PARSER ###

# build argument parser
parser = argparse.ArgumentParser(add_help=False)

parser.add_argument('-to', '--timeout', type=int, default=5)
parser.add_argument('-i', '--interface', type=str, default='wlan0')
parser.add_argument('-h', '--help', action='store_true')
parser.add_argument('--debug', action='store_true')

# parse passed argumentation
args = parser.parse_args()

if args.timeout is not None and args.timeout not in range(1,1000):
	print(f'\n Timeout must be between 1 and 1000 \n')
	exit()
