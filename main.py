#!/usr/bin/python

import sys

from parkingLot import ParkingLot

def main(argv=None):
	if argv is None:
		argv = sys.argv
	parkinglot = ParkingLot(int(argv[1]))



if __name__ == '__main__':
    main()