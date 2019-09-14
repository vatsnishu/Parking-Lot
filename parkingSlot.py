#!/usr/bin/python

from car import Car

class ParkingSlot:
	def __init__(self, id):
		self.status = "empty"
		self.carParked = None
		self.id = id
		print("parking slot initialised with id {0}").format(id)

	def parkCar(self, carParked):
		self.status = "occupied"
		self.carParked = carParked
		print("parked car")

	def freeTheSlot(self):
		self.status = "empty"
		self.carParked = None
		print("free slot")