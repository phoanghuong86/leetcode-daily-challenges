class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # stack contains [x,y] pairs representing [char, consecutive appearances]
        stack = []
        for char in s:
            # If current char matches char at top of the stack
            if len(stack) > 0 and char == stack[-1][0]:
                # Increment the counter for the char
                stack[-1][1] += 1
                # If the counter has reached k, pop the char
                if stack[-1][1] == k:
                    del stack[-1]
            else:
                # Add new char to the stack
                stack.append([char, 1])
        
        # Construct solution string based on stack
        sol = ''
        for pair in stack:
            sol += pair[0] * pair[1]
        
        return sol
