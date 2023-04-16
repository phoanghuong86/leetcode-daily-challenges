class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        
        # Create a dictionary with keys as characters from 'a' to 'z'
        # and values as a list of zeros with length equal to the length of words[0]
        char_count = {
            char: [0]*len(words[0])
            for char in string.ascii_lowercase
        }
        
        # Initialize mod as 10^9 + 7
        mod = 10**9+7

        # Count the number of occurrences of each character in each position of words
        for word in words:
            for i, c in enumerate(word):
                char_count[c][i] += 1


        @cache
        def func(i, j):
            '''
            i : target[i],
            j : word[j]
            '''
            # Base case: when all characters of target have been used
            if i == -1:
                return 1
            # Base case: when all words have been used, but some characters of target are still remaining
            elif j == -1:
                return 0
            # Recurrence relation: number of ways to form target[i:] from words[j:] 
            # = number of ways to form target[i:] from words[:j-1] (without using words[j-1][k])
            # + number of ways to form target[i+1:] from words[:j-1] (using words[j-1][k] for target[i])
            # * number of occurrences of target[i] at position j-1 in words
            return (func(i, j-1) + func(i-1, j-1)*char_count[target[i]][j])%mod
        
        # Call the recursive function with starting indices (len(target)-1, len(words[0])-1)
        # i.e., start forming target from the last character and words from the last position
        return func(len(target)-1, len(words[0])-1)
