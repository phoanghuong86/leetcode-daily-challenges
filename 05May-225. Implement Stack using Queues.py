class MyStack:
    def __init__(self):
        self.queue1 = []
        self.queue2 = []
        
    def push(self, x: int) -> None:
        self.queue1.append(x)

    def pop(self) -> int:
        l = len(self.queue1)
        while l > 1:
            cur = self.queue1.pop(0)
            self.queue2.append(cur)
            l-=1
        last = self.queue1.pop(0)
        self.queue1 = self.queue2
        return last
            
    def top(self) -> int:
        return self.queue1[len(self.queue1)-1]

    def empty(self) -> bool:
        if not self.queue1:
            return True
        else:
            return False



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
