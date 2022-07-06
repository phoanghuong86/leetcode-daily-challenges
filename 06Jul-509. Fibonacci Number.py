class Solution:
    def fib(self, n: int) -> int:
        arr = [0,1]
        for i in range(2,31):
            # print(arr[i-2])
            # print(arr[0])
            arr.append(arr[i-1] + arr[i-2])
        return arr[n]
