class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [-1] * k
        self.front = self.back = self.count = 0
        self.k = k

    def enQueue(self, value: int) -> bool:
        if self.count < self.k:
            self.queue[self.back] = value
            self.count += 1
            self.back = (self.back + 1) % self.k
            return True

    def deQueue(self) -> bool:
        if self.queue[self.front] != -1:
            self.queue[self.front] = -1
            self.count -= 1
            self.front = (self.front + 1) % self.k
            return True
        
    def Front(self) -> int:
        return self.queue[self.front]

    def Rear(self) -> int:
        return self.queue[self.back - 1]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.k

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
