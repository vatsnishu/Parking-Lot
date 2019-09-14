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
	f = open("bin/parking_lot file_inputs.txt")
	inputsFromFile = f.readlines()
	for inputs in inputsFromFile:
		inputs = inputs.strip('\n')
		command = inputs.split(' ')
		if command[0] == "create_parking_lot" and len(command) == 2:
			parkinglot = ParkingLot(int(command[1]))
		elif command[0] == "park" and len(command) == 3:
			try:
				parkinglot.park(color=command[2], registrationNumber=command[1])
			except Exception as e:
				exceptionOccurred(exception=e)
		elif command[0] == "status" and len(command) == 1:
			parkinglot.status()
		elif command[0] == "leave" and len(command) == 2:
			parkinglot.leave(int(command[1]))
		elif command[0] == "slot_numbers_for_cars_with_colour" and len(command) == 2:
			parkinglot.slotNumbersOfCarWithGivenColour(command[1])
		elif command[0] == "registration_numbers_for_cars_with_colour" and len(command) == 2:
			parkinglot.registrationNumbersOfCarWithGivenColour(command[1])
		elif command[0] == "slot_number_for_registration_number" and len(command) == 2:
			parkinglot.slotNumberCarWithGivenRegistrationNumber(command[1])
		elif command[0] == "exit" and len(command) == 1:
			exit(0)
		else:
			printHelp()



if __name__ == '__main__':
    main()