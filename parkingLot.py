#!/usr/bin/python

from parkingSlot import ParkingSlot
from collections import OrderedDict 
from car import Car
from ticket import Ticket

class ParkingLot:
	def __init__(self, maxNumberOfSlots=0):
		self.maxNumberOfSlots = maxNumberOfSlots
		self.availableSlots = {}
		self.allSlots = list()
		self.tickets = {}
		self.ticketId = 1
		for i in range(maxNumberOfSlots):
			slot = ParkingSlot(id=i+1)
			self.availableSlots[i+1] = slot
		print("Created a parking lot with {0} slots").format(maxNumberOfSlots)

	def park(self, color, registrationNumber):
		if(len(self.availableSlots) == 0):
			print("Sorry, parking lot is full")
			return
		minSlotId = min(self.availableSlots.keys(), key=(lambda k: self.availableSlots[k]))
		slot = self.availableSlots[minSlotId]
		del self.availableSlots[minSlotId]
		car = Car(registrationNumber=registrationNumber, color=color)
		ticket = self.generateTicket()
		ticket.assignTicket(car=car,slot=slot)
		car.carGetsParked(ticket)
		slot.parkCar(carParked=car)
		print("Allocated slot number: {0}").format(slot.id)

	def generateTicket(self):
		ticket = Ticket(self.ticketId)
		self.tickets[self.ticketId] = ticket
		self.ticketId += 1;
		return ticket

	def revokeTicket(self, ticketId):
		del self.tickets[ticketId]

	def leave(self, ticketId):
		ticket = self.tickets[ticketId]
		if ticket is None:
			print("Ticket ID is invalid")
			return
		car = ticket.car
		slot = ticket.slot
		self.revokeTicket(ticket.id)
		slot.freeTheSlot()
		car.carLeaves()
		self.availableSlots[slot.id] = slot
		print("Slot number {0} is free").format(slot.id)

	def status(self):
		print("Slot No.    Registration No    Colour")
		for ticket in sorted(self.tickets.values(), key = lambda x : x.slot.id):
			print("{0}           {1}      {2}").format(ticket.slot.id, ticket.car.registrationNumber, ticket.car.color)


	def  ticketNumbersOfCarWithGivenColour(self, color):
		listOfTickets = []
		for ticket in sorted(self.tickets.values(), key = lambda x : x.slot.id):
			if ticket.car.color == color:
				listOfTickets.append(ticket)
		return listOfTickets


	def slotNumbersOfCarWithGivenColour(self, color):
		listOfTickets = self.ticketNumbersOfCarWithGivenColour(color)
		resultString = ""
		if(len(listOfTickets) == 0):
			return None
		i=0
		for ticket in sorted(listOfTickets):
			if(i!=0):
				resultString += ", "
			i+=1
			resultString += str(ticket.slot.id)
		return resultString

	def registrationNumbersOfCarWithGivenColour(self, color):
		listOfTickets = self.ticketNumbersOfCarWithGivenColour(color)
		resultString = ""
		if(len(listOfTickets) == 0):
			return None
		i=0
		for ticket in listOfTickets:
			if(i!=0):
				resultString += ", "
			resultString += ticket.car.registrationNumber
			i+=1
		return resultString

	def  slotNumberCarWithGivenRegistrationNumber(self, registrationNumber):
		for ticket in sorted(self.tickets.values(), key = lambda x : x.slot.id):
			if ticket.car.registrationNumber == registrationNumber:
				return 	ticket.slot.id
		return None







