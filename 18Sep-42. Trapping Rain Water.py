class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        total = 0
        for h in height:
            if stack and h >= stack[0]:
                for s in stack:
                    total += stack[0] - s
                stack = [h]
            else:
                stack.append(h)
        
        h = stack.pop()
        while stack:
            if stack[-1] < h:
                total += h - stack.pop()
            else:
                h = stack.pop()
        
        return total
