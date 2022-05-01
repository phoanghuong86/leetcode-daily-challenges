class Solution:
    def backspaceCompare(self, S, T):
        l1 = self.stack(S, [])
        l2 = self.stack(T, [])
        return l1 == l2
        
    
    def stack(self, S, stack):
        for char in S:
            if char is not "#":
                stack.append(char)
            else:
                if not stack:
                    continue
                stack.pop()
        return stack
