class Solution:
    def calculate(self, s):    
        def calc(it):
            def update(op, v):
                if op == "+": stack.append(v)
                if op == "-": stack.append(-v)
        
            num, stack, sign = 0, [], "+"
            
            while it < len(s):
                if s[it].isdigit():
                    num = num * 10 + int(s[it])
                elif s[it] in "+-*/":
                    # store existing num onto stack
                    update(sign, num)
                    # start new num with 0
                    num, sign = 0, s[it]
                elif s[it] == "(":
                    num, it = calc(it + 1) # start new recursion
                elif s[it] == ")":
                    # num ends here, store it on stack
                    update(sign, num)
                    # unwind recursion
                    return sum(stack), it
                it += 1
            update(sign, num)
            return sum(stack)

        return calc(0)
