from model.ParkingLot import ParkingLot
from model.Vehicle import Vehicle



if __name__ == "__main__":

    parkingLot = ParkingLot(5)

    v1 = Vehicle('KA-01-HH-1234', 'White')
    v2 = Vehicle('KA-01-HH-9999', 'White')
    v3 = Vehicle('KA-01-BB-0001', 'Black')
    v4 = Vehicle('KA-01-HH-7777', 'Red')

    parkingLot.entryCar(v1)
    parkingLot.entryCar(v2)
    parkingLot.entryCar(v3)
    parkingLot.entryCar(v4)
    print(parkingLot.getSlotsByColor('White'))

    parkingLot.exitSlot(1)

    v5 = Vehicle('KA-01-HH-2403', 'Blue')
    parkingLot.entryCar(v5)
    print(parkingLot.getPlateByColor('Blue'))


    v6 = Vehicle('KA-01-HH-1111', 'Blue')
    v7 = Vehicle('KA-01-HH-2222', 'Blue')
    parkingLot.entryCar(v6)
    parkingLot.entryCar(v7)
