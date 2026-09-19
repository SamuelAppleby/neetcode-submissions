import bisect
class MinStack:

    def __init__(self):
        self.__stack = []
        self.__min_order = []

    def push(self, val: int) -> None:
        self.__stack.append(val)
        bisect.insort(self.__min_order, val)

    def pop(self) -> None:
        popped = self.__stack.pop()
        self.__min_order.remove(popped)

    def top(self) -> int:
        return self.__stack[-1]

    def getMin(self) -> int:
        return self.__min_order[0]
