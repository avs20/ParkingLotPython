class Slot:
    def __init__(self, number):
        self.number = number
        self.vehicle = None
        self.occupied = False

    def allotVehicle(self, vehicle):
        self.vehicle = vehicle
        self.occupied = True 
        

    def freeSpace(self):
        vehicle = self.vehicle
        self.occupied = False
        self.vehicle = None
        return vehicle


