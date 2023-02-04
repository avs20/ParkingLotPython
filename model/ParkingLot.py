from .Slot import Slot
from .Vehicle import Vehicle
from .NearestAllocationStrategy import NearestAllocationStrategy

class ParkingLot:

    def __init__(self, numSlots) -> None:
        self.slots = [None]
        for ix in range (1,numSlots + 1):
            self.slots.append(Slot(ix))
        
        self.AllocationStrategy = NearestAllocationStrategy(self.slots)
        self.colorMap = {}
        self.plateMap = {}
    

    def entryCar(self, vehicle):
        nextPosition = self.AllocationStrategy.getNextSlot()

        if nextPosition:
            slot = self.slots[nextPosition]
            slot.allotVehicle(vehicle)
            self.addToColorIndex(vehicle,slot)
            self.addToPlateIndex(vehicle, slot)
            return True 
            
        else:
            print("Sorry, parking lot is full!")
            return False 
    
    def exitSlot(self, slotNum):

        slot = self.slots[slotNum]
        if not slot.occupied:
            raise Exception("Slot {} is not occupied".format(slot.number))
        
        vehicle = slot.freeSpace()
        self.removeFromColorIndex(vehicle, slot)
        self.removeFromPlateIndex(vehicle, slot)

        print("Slot {} is free".format(slot.number))
        return True 

    def addToColorIndex(self, vehicle, slot):
        
        if vehicle.color not in self.colorMap:
            self.colorMap[vehicle.color] = []
        
        self.colorMap[vehicle.color].append(slot)

    def addToPlateIndex(self, vehicle, slot):

        if vehicle.plate not in self.plateMap:
            self.plateMap[vehicle.plate] = slot
        
    
    def removeFromColorIndex(self, vehicle, slot):

         self.colorMap[vehicle.color].remove(slot)

    
    def removeFromPlateIndex(self, vehicle, slot):

        del self.plateMap[vehicle.plate]


    
    def getPlateByColor(self, color):

        if color not in self.colorMap:
            return None 

        return [slot.vehicle.plate for slot in self.colorMap[color]]

    
    def getSlotByPlate(self, plate):

        if plate not in self.plateMap:
            return None
        
        return self.plateMap[plate]

    
    def getSlotsByColor(self, color):

        if color not in self.colorMap:
            return None 

        return self.colorMap[color]
    

        
        


        

