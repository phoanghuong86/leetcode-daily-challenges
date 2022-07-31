class NumArray:

    def __init__(self, nums: List[int]):
        self.data = nums
        self.n = int(len(nums)**0.5//1)
        self.blocks = [0]*(self.n+2)
        for i in range(len(nums)):
            self.blocks[i // self.n] += nums[i]
            

    def update(self, index: int, val: int) -> None:
        delta = val - self.data[index]
        self.data[index] = val
        self.blocks[index//self.n] += delta
        

    def sumRange(self, left: int, right: int) -> int:
        sum_value = 0
        
        if right - left > self.n:
            for i in range(left, ((left//self.n)+1)*self.n):
                sum_value += self.data[i]
                
            for i in range((right//self.n)*self.n, right + 1):
                sum_value += self.data[i]
        
            for i in range((left // self.n)+1, right //self.n):
                sum_value += self.blocks[i]

        else:
            for i in range(left, right+1):
                sum_value += self.data[i]

        return sum_value
