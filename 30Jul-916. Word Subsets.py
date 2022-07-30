class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        """
        Keep track of the maximum count for each character among all words in words2. Ex: given words 'good' and 'hot', good has 2 o's and hot has 1 o, so we would have counts2['o'] = 2 since good has more o's than hot. 
        If a word is universal, then all it character counts should be greater than all the character counts in counts2. 
        """
        res = []
        words2Set = set(words2)
        counts2 = Counter("")
        for w2 in words2Set:
            counts2 = counts2 | Counter(w2) # The | operator joins the two Counters together, keeping the max count of each key between both Counters. 
        for word1 in words1:
            good = True
            counts1 = Counter(word1)
            if counts1 | counts2 == counts1: # If this is false, then that means that there is a character count in counts2 that is greater than the coresponding character count in counts1. 
                res.append(word1)
        return res
