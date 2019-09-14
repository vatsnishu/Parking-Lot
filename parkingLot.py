#!/usr/bin/python

from parkingSlot import ParkingSlot

class ParkingLot:
	def __init__(self, maxNumberOfSlots=0):
		self.maxNumberOfSlots = maxNumberOfSlots
		self.availableSlotList = list()
		for i in range(maxNumberOfSlots):
			slot = ParkingSlot(id=i+1)
			self.availableSlotList.append(slot)

