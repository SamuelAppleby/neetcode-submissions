class DynamicArray:
    
    def __init__(self, capacity: int):
        self.array = [None] * capacity


    def get(self, i: int) -> int:
        return self.array[i]


    def set(self, i: int, n: int) -> None:
        self.array[i] = n


    def pushback(self, n: int) -> None:
        for i in range(0, len(self.array), 1):
            if self.array[i] is None:
                self.set(i, n)
                return
        
        final = len(self.array)
        self.resize()
        self.set(final, n)


    def popback(self) -> int:
        for i in range(0, len(self.array), 1):
            if self.array[i] is None:
                tmp = self.array[i-1]
                self.array[i-1] = None
                return tmp

        tmp = self.array[-1]
        self.array[-1] = None
        return tmp
 

    def resize(self) -> None:
        self.array.extend([None] * len(self.array))


    def getSize(self) -> int:
        return len([a for a in self.array if a is not None])
        
    
    def getCapacity(self) -> int:
        return len(self.array)
