#!/usr/bin/python

import sys

from parkingLot import ParkingLot

def main(argv=None):
	if argv is None:
		argv = sys.argv
	command = sys.argv[1]
	parkinglot = ParkingLot(int(argv[1]))
	parkinglot.park(color="White", registrationNumber="KA-01-HH-1234")
	parkinglot.park(color="White", registrationNumber="KA-01-HH-9999")
	parkinglot.park(color="Black", registrationNumber="KA-01-BB-0001")
	parkinglot.park(color="Red", registrationNumber="KA-01-HH-7777")
	parkinglot.park(color="Blue", registrationNumber="KA-01-HH-2701")
	parkinglot.leave(4)
	parkinglot.park(color="Black", registrationNumber="KA-01-HH-3141")



if __name__ == '__main__':
    main()