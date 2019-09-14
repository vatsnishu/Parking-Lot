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
	helpString = "\nPlease enter commands in following form:\ncreate_parking_lot $numberOfParkingSlots\npark $carNumber $carColor\nleave $parkingTicketNumber\nstatus\nregistration_numbers_for_cars_with_colour $color\nslot_numbers_for_cars_with_colour $color\nexit"
	print(helpString)

def main(argv=None):
	# takes input from command line
	if len(sys.argv) == 1:
		parkinglot = None
		while(1):
			inputs = raw_input()
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
				resultString = parkinglot.slotNumbersOfCarWithGivenColour(command[1])
				if resultString is None:
					print("Not found")
				else:
					print(resultString)
			elif command[0] == "registration_numbers_for_cars_with_colour" and len(command) == 2:
				resultString = parkinglot.registrationNumbersOfCarWithGivenColour(command[1])
				if resultString is None:
					print("Not found")
				else:
					print(resultString)
			elif command[0] == "slot_number_for_registration_number" and len(command) == 2:
				slotID = parkinglot.slotNumberCarWithGivenRegistrationNumber(command[1])
				if slotID is None:
					print(slotID)
				else:
					print("Not found")
			elif command[0] == "exit" and len(command) == 1:
				exit(0)
			else:
				printHelp()
	#takes input from file
	else:
		parkinglot = None
		f = open(sys.argv[1])
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
				resultString = parkinglot.slotNumbersOfCarWithGivenColour(command[1])
				if resultString is None:
					print("Not found")
				else:
					print(resultString)
			elif command[0] == "registration_numbers_for_cars_with_colour" and len(command) == 2:
				resultString = parkinglot.registrationNumbersOfCarWithGivenColour(command[1])
				if resultString is None:
					print("Not found")
				else:
					print(resultString)
			elif command[0] == "slot_number_for_registration_number" and len(command) == 2:
				slotID = parkinglot.slotNumberCarWithGivenRegistrationNumber(command[1])
				if slotID is None:
					print("Not found")
				else:
					print(slotID)
			elif command[0] == "exit" and len(command) == 1:
				exit(0)
			else:
				printHelp()



if __name__ == '__main__':
    main()