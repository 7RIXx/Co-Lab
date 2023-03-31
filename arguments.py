#!/bin/env python3

import argparse
import psutil

help_menu = '''

	PLACEHOLDER FOR ASCII ART

	
	-i, --interface :: Set interface (eg. wlan0)
	
	-to, --timeout :: Set a timeout delay (Range 1-1000)
	
	-h, --help :: Show this menu
	
	--debug :: Shows various developing cues used in production
	
	





'''







### ARGUMENT PARSER ###

# build argument parser
parser = argparse.ArgumentParser(add_help=False)

parser.add_argument('-i', '--interface', type=str)
parser.add_argument('-to', '--timeout', type=int)
parser.add_argument('-h', '--help', action='store_true')
parser.add_argument('--debug', action='store_true')

# parse passed argumentation
args = parser.parse_args()

if args.interface not in psutil.net_if_addrs():
	print(f'\n {help_menu} \n)
	exit()
if args.timeout not in range(1,1000):
	print(f'\n {help_menu} \n)
	exit()
