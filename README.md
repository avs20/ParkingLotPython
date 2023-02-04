N cars
1 with distance 

ticket
    number plate, color, allocation 


book nearest to entry slot 
exit - mark the slot as empty. 


search by 
    find all cars by color 
    give plate number find slot 
    find all the slots by color.


Parking lot 
Parking Lot has slots 
Parking lot allocates slot by an AllocationStrategy (Nearest in this case)
Slots have Vehicles
Vehicles have 
    color
    plate No 


How to search - 
    color : List of slots 
    plateNumber : slot 


AllocationStrategy Interface:
    getNextSlot()
    