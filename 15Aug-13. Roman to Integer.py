
class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        int_val = previous_val = roman[s[-1]]
        for idx in range(len(s)-2, -1, -1):
            current_val = roman[s[idx]]
            if current_val >= previous_val:
                int_val += current_val
            elif current_val < previous_val:
                int_val -= current_val
            previous_val = current_val
        return int_val
