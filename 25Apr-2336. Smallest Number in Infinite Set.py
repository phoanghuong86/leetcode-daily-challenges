class SmallestInfiniteSet:

    def __init__(self):
        self.current = 1
        self.arr = []

    def popSmallest(self) -> int:
        if not self.arr:
            result = self.current
            self.current += 1
            return result
        return heappop(self.arr)

    def addBack(self, num: int) -> None:
        if self.current > num and num not in self.arr:
            heappush(self.arr, num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
