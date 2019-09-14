#!/usr/bin/python

from car import Car

class ParkingSlot:
	def __init__(self, id):
		self.status = "empty"
		self.carParked = None
		self.id = id

	def parkCar(self, carParked):
		self.status = "occupied"
		self.carParked = carParked

	def freeTheSlot(self):
		self.status = "empty"
		self.carParked = None