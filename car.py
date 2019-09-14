#!/usr/bin/python

class Car:
	def __init__(self, registrationNumber, color):
		self.registrationNumber = registrationNumber
		self.color = color
		self.assignedTicket = None

	def carLeaves(self):
		print("car removed from slot {0} and ticket if assigned is {1}").format(self.assignedTicket.slot.id, self.assignedTicket.id)
		self.assignedTicket = None


	def carGetsParked(self, assignedTicket):
		self.assignedTicket = assignedTicket
		print("car parked in slot {0} and ticket if assigned is {1}").format(assignedTicket.slot.id, assignedTicket.id)