class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        stack = []

        for char in s:
            if char in mapping:
                if not stack or mapping[char] != stack.pop():
                    return False

            else:
                stack.append(char)

        return not stack
