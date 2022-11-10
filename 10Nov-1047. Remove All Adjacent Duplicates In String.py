class Solution:
    def removeDuplicates(self, s: str) -> str:
    	### initialize an empty stack
        stack = []

        for char in s:
        	
        	### This is the case where two adjacent letters are equal
        	### don't store it and pop the last one from stack,
        	### Don't forget to check if the stack is empty!
            if stack and char==stack[-1]:
                stack.pop()

            else:
                stack.append(char)
        
        return ''.join(stack)
