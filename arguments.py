#!/bin/env python3

import argparse, psutil, os







### ARGUMENT PARSER ###

# build argument parser
parser = argparse.ArgumentParser(add_help=False)

parser.add_argument('-sf', '--sniff', action='store_true')
parser.add_argument('-sp', '--snoop', action='store_true')
parser.add_argument('-o', '--output', type=str)
parser.add_argument('-H', '--hidden', action='store_true')
parser.add_argument('-to', '--timeout', type=int)
parser.add_argument('-q', '--quick', action='store_true')
parser.add_argument('-h', '--help', action='store_true')
parser.add_argument('--credits', action='store_true')
parser.add_argument('--debug', action='store_true')

# parse passed argumentation
args = parser.parse_args()

if args.credits:
	helpers.roll_credits()
	exit()

if args.sniff and args.snoop is not None:
	print(f' Please choose either Sniff or Snoop ')
	exit()

if args.output is not None:
	try:
		args.output = args.output.split('.')[0]
	except:
		pass

if args.timeout is not None and args.timeout not in range(1,1000):
	print(f'\n Timeout must be between 1 and 1000 \n')
	exit()
elif args.timeout is not None:
	args.timeout = int(args.timeout)
else:
	args.timeout = 512




