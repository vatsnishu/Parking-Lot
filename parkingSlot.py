#!/usr/bin/python

from car import Car

class ParkingSlot:
	def __init__(self, id, status="empty", carParked=None):
		self.status = status
		self.carParked = carParked
		print("parking slot initialised with id {0}").format(id)