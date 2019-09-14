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
			self.availableSlots[i] = slot
			self.allSlots = slot

	def park(self, color, registrationNumber):
		minSlotId = min(self.availableSlots.keys(), key=(lambda k: self.availableSlots[k]))
		slot = self.availableSlots[minSlotId]
		del self.availableSlots[minSlotId]
		car = Car(registrationNumber=registrationNumber, color=color)
		ticket = self.generateTicket()
		ticket.assignTicket(car=car,slot=slot)
		car.carGetsParked(ticket)
		slot.parkCar(carParked=car)

	def generateTicket(self):
		ticket = Ticket(self.ticketId)
		self.tickets[self.ticketId] = ticket
		self.ticketId += 1;
		return ticket

	def revokeTicket(self, ticketId):
		del self.tickets[ticketId]

	def leave(self, ticketId):
		ticket = self.tickets[ticketId]
		car = ticket.car
		slot = ticket.slot
		self.revokeTicket(ticket.id)
		slot.freeTheSlot()
		car.carLeaves()
		self.availableSlots[slot.id] = slot

	def  ticketsOfCarWithGivenColour(self, color):
		listOfTickets = []
		for ticket in self.tickets:
			if ticket.car.color == color:
				listOfTickets.append(ticket)

	def  ticketsOfCarWithGivenRegistrationNumber(self, registrationNumber):
		listOfTickets = []
		for ticket in self.tickets:
			if ticket.car.registrationNumber == registrationNumber:
				listOfTickets.append(ticket)			






