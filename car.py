#!/usr/bin/python

class Car:
	def __init__(self, registrationNumber, color):
		self.registrationNumber = registrationNumber
		self.color = color
		self.assignedTicket = None

	def carLeaves(self):
		self.assignedTicket = None


	def carGetsParked(self, assignedTicket):
		self.assignedTicket = assignedTicket