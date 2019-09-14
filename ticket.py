#!/usr/bin/python

from parkingSlot import ParkingSlot 

from car import Car

class Ticket:
	def __init__(self, id):
		self.car = None
		self.slot = None
		self.id = id

	def assignTicket(self, car, slot):
		self.car = car
		self.slot = slot