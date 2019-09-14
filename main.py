#!/usr/bin/python

import sys

from parkingLot import ParkingLot

def exceptionOccurred(exception=None):
	if exception is not None:
		print("Exception occurred {0}").format(exception.args)
	else:
		print("Exception occurred")
	exit(1)

def printHelp():
	helpString = ""


def main(argv=None):
	parkinglot = None
	while(1):
		inputByUser = raw_input()
		command = inputByUser.split(' ')
		if command[0] == "create_parking_lot":
			parkinglot = ParkingLot(int(command[1]))
		elif command[0] == "park":
			try:
				parkinglot.park(color=command[2], registrationNumber=command[1])
			except Exception as e:
				exceptionOccurred(exception=e)
		elif command[0] == "status":
			parkinglot.status()
		elif command[0] == "leave":
			parkinglot.leave(command[1])
		elif command[0] == "exit":
			exit(0)
		else:
			printHelp()



if __name__ == '__main__':
    main()