class MyCircularQueue:

    def __init__(self, k: int):
        self.cq = [None] * k
        self.size = k
        self.f = 0
        self.r = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.cq[self.r] = value
        self.r = (self.r + 1) % self.size
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.cq[self.f] = None
        self.f = (self.f + 1) % self.size
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.cq[self.f]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.cq[self.r - 1]

    def isEmpty(self) -> bool:
        return True if self.f == self.r and self.cq[self.f] is None else False

    def isFull(self) -> bool:
        return True if self.f == self.r and self.cq[self.f] is not None else False
