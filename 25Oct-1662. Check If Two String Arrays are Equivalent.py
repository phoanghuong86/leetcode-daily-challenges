from itertools import zip_longest

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        
        # [1] here, we construct generators (not lists!) that
        #     yield (!) characters from each word
        gen1 = (ch1 for w1 in word1 for ch1 in w1)
        gen2 = (ch2 for w2 in word2 for ch2 in w2)
        
        # [2] zip_longest from itertools ensures that
        #     different lengths are treated correctly
        return all(ch1 == ch2 for ch1, ch2 in zip_longest(gen1, gen2))
