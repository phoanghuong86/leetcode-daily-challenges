class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        rows_queue = {
            i: "" for i in range(numRows)
        }
        ptr, down = 0, True
        for letter in s:
            rows_queue[ptr]+= letter
            if down:
                ptr += 1
            else:
                ptr -= 1

            if ptr == 0:
                down = True
            elif ptr == numRows - 1:
                down = False
        
        ans = ""
        for i in range(numRows):
            ans += rows_queue[i]

        return ans
