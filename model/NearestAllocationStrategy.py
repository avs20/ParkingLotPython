from heapq import *
class NearestAllocationStrategy:
    """
    What I want is the next slot which is empty and closest to entry 
    So the position with lowest value which is empty. 
    I think a minheap will be best. 
    It will be getting available slots from minHeap and adding free slots to minHeap
    """

    def __init__(self, slots) -> None:        
        self.minHeap = []
        for slot in slots[1:]:
            self.minHeap.append(slot.number)
            heapify(self.minHeap)
        


    def getNextSlot(self):
        if len(self.minHeap):
            nextPosition = heappop(self.minHeap)
            return nextPosition
        else:
            return None
    
    def addFreeSlot(self, slot):
        heappush(self.minHeap, slot.number)
    
