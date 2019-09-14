#!/usr/bin/python

import unittest
from parkingLot import ParkingLot
from ticket import Ticket
from car import Car
from parkingSlot import ParkingSlot

TOTAL_PARKING_SLOTS = 8

class TestParkingLotMethods(unittest.TestCase):
    def test_init_parking_lot(self):
        self.parkingLot = ParkingLot(TOTAL_PARKING_SLOTS)
        self.assertEqual(self.parkingLot.maxNumberOfSlots, 8)
        self.assertEqual(len(self.parkingLot.tickets), 0)
        self.assertEqual(self.parkingLot.ticketId, 1)
        self.assertEqual(len(self.parkingLot.availableSlots), 8)


    def test_park(self):
        self.parkingLot = ParkingLot(TOTAL_PARKING_SLOTS)
        self.parkingLot.park(color="Red", registrationNumber="KA-01-HH-1234")
        car = self.parkingLot.tickets[1].car
        slot = self.parkingLot.tickets[1].slot
        self.assertEqual(len(self.parkingLot.tickets), 1)
        self.assertEqual(self.parkingLot.ticketId, 2)
        self.assertEqual(len(self.parkingLot.availableSlots), 7)
        self.assertEqual(self.parkingLot.maxNumberOfSlots, 8)
        self.assertEqual(car.color, "Red")
        self.assertEqual(car.registrationNumber, "KA-01-HH-1234")

    def test_leave(self):
        self.parkingLot = ParkingLot(TOTAL_PARKING_SLOTS)
        self.parkingLot.park(color="Red", registrationNumber="KA-01-HH-1234")
        self.parkingLot.leave(1)
        self.assertFalse(self.parkingLot.tickets.has_key(1))
        self.assertEqual(len(self.parkingLot.tickets), 0)
        self.assertEqual(self.parkingLot.ticketId, 2)
        self.assertEqual(len(self.parkingLot.availableSlots), 8)
        self.assertEqual(self.parkingLot.maxNumberOfSlots, 8)

    def  test_ticketNumbersOfCarWithGivenColour(self):
        self.parkingLot = ParkingLot(TOTAL_PARKING_SLOTS)
        self.parkingLot.park(color="Red", registrationNumber="KA-01-HH-1234")
        self.parkingLot.park(color="Red", registrationNumber="KA-01-HH-5555")
        listOfTickets = self.parkingLot.ticketNumbersOfCarWithGivenColour("Red")
        listOfTicketsNegative = self.parkingLot.ticketNumbersOfCarWithGivenColour("White")
        self.assertEqual(len(listOfTickets), 2)
        self.assertEqual(listOfTickets[0].car.color, "Red")
        self.assertEqual(listOfTickets[1].car.color, "Red")
        self.assertEqual(len(listOfTicketsNegative), 0)

    def test_slotNumbersOfCarWithGivenColour(self):
        self.parkingLot = ParkingLot(TOTAL_PARKING_SLOTS)
        self.parkingLot.park(color="Red", registrationNumber="KA-01-HH-1234")
        self.parkingLot.park(color="Red", registrationNumber="KA-01-HH-5555")
        listOfSlots = self.parkingLot.slotNumbersOfCarWithGivenColour("Red")
        listOfSlotsNegative = self.parkingLot.slotNumbersOfCarWithGivenColour("White")
        self.assertIsNone(listOfSlotsNegative)
        self.assertIsNotNone(listOfSlots)

    def test_registrationNumbersOfCarWithGivenColour(self):
        self.parkingLot = ParkingLot(TOTAL_PARKING_SLOTS)
        self.parkingLot.park(color="Red", registrationNumber="KA-01-HH-1234")
        self.parkingLot.park(color="Red", registrationNumber="KA-01-HH-5555")
        listOfRegistrationNumbers = self.parkingLot.registrationNumbersOfCarWithGivenColour("Red")
        listOfRegistrationNumbersNegative = self.parkingLot.registrationNumbersOfCarWithGivenColour("White")
        self.assertNotEqual(listOfRegistrationNumbers.find("KA-01-HH-1234"), -1)
        self.assertNotEqual(listOfRegistrationNumbers.find("KA-01-HH-5555"), -1)
        self.assertIsNone(listOfRegistrationNumbersNegative)

    def  test_slotNumberCarWithGivenRegistrationNumber(self):
        self.parkingLot = ParkingLot(TOTAL_PARKING_SLOTS)
        self.parkingLot.park(color="Red", registrationNumber="KA-01-HH-1234")
        self.parkingLot.park(color="Red", registrationNumber="KA-01-HH-5555")
        slotId1 = self.parkingLot.slotNumberCarWithGivenRegistrationNumber("KA-01-HH-1234")
        slotId2 = self.parkingLot.slotNumberCarWithGivenRegistrationNumber("KA-01-HH-5555")
        slotIdNegative = self.parkingLot.slotNumberCarWithGivenRegistrationNumber("KA-01-HH-yyyy")
        self.assertEqual(slotId1, 1)
        self.assertEqual(slotId2, 2)
        self.assertIsNone(slotIdNegative)


if __name__ == '__main__':
    unittest.main()