class LinkedList:
    
    def __init__(self):
        self.lst = []
    
    def get(self, index: int) -> int:
        if index > len(self.lst) - 1:
            return -1

        return self.lst[index]
        

    def insertHead(self, val: int) -> None:
        self.lst.insert(0, val)
        

    def insertTail(self, val: int) -> None:
        self.lst.append(val)
        

    def remove(self, index: int) -> bool:
        if index > len(self.lst) - 1:
            return False
        
        self.lst.pop(index)
        return True
        

    def getValues(self) -> List[int]:
        return self.lst            
        
