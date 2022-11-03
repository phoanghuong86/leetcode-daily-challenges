class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        from collections import defaultdict
        
        seen = defaultdict(int)
        result = 0

        for word in words:
            complement = word[1] + word[0] 
            if seen[complement] > 0:  
                # can match word with a complement to increase length of the palindrome by 4
                result += 4
                seen[complement] -= 1
                if seen[complement]==0:
                    del seen[complement]  # to free up memory
            else:
                seen[word] += 1
        
        # if there is at least one duplicate pair left in seen,
        # we can use it for only once in the palindrome, at the center.
        for word in seen:
            if seen[word] > 0 and word[0] == word[1]:
                result += 2
                break
                
        return result  
