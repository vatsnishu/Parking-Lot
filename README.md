This app simulates the day to day operations of a parking lot. Given a parking lot with a specific number of parking spots, vehicles will both enter and exit. When entering a vehicle is given the choice of parking spot size (sm, md, lg) depending on the size of the vehicle (sm, md, lg). Vehicles may only park in parking spaces of equal or greater size. Once entered, a ticket is opened and assigned to the vehicle. When the vehicle exits the parking lot, the ticket is closed.

This project is the object-orient solution of the parking lot problem.

The python version is 2.7

execute main.py to simulate the parking action

The description of the problem is as follows:

There is a roboticized parking lot that has no human managers

There are specific number of parking slots. Each slot is given a number starting at 1 increasing with increasing distance from the entry point in steps of one. I want to create an automated ticketing system that allows my customers to use my parking lot without human intervention.

Cars will both enter and exit. When a car enters my parking lot, I want to have a ticket issued to the driver. The ticket issuing process includes us documenting the registration number (number plate) and the colour of the car and allocating an available parking slot to the car before actually handing over a ticket to the driver (If there is not enough space for parking, error with parking full will be printed). 

The customer should be allocated a parking slot which is nearest to the entry. At the exit the customer returns the ticket which then marks the slot they were using as being available.

Due to government regulation, the system provides with the ability to find out:
● Registration numbers of all cars of a particular colour.(registration_numbers_for_cars_with_colour $color)
● Slot number in which a car with a given registration number is parked.(slot_number_for_registration_number $color)
● Slot numbers of all slots where a car of a particular colour is parked.(slot_numbers_for_cars_with_colour $color)

We interact with the system via a simple set of commands which produce a specific output.

Please enter commands in following form:

create_parking_lot $numberOfParkingSlots
park $carNumber $carColor
leave $parkingTicketNumber
status
registration_numbers_for_cars_with_colour $color
slot_numbers_for_cars_with_colour $color
exit

The system should allows input in following two ways.

1) It provides us with an interactive command prompt based shell where commands can be typed in. If filename is not given as second argument, system automatically reads input from shell terminal.
2) It accepts a filename as a parameter at the command prompt and read the commands from that file. If filename is given as command line argument then program reads commands from file.




