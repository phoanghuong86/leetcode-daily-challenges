class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        map = {}
        for i in range(len(order)):
            map[order[i]] = i
        map['@'] = -1 
        def compare(s1, s2):
            if len(s2) <= len(s1):
                s2 += "@"*(len(s1)- len(s2))
            else:
                s1 += "@"*(len(s2)- len(s1))
            for i in range(len(s1)):
                if s1[i] == s2[i]:
                    continue  
                elif map[s1[i]] > map[s2[i]]:
                    return False
                else:
                    break
            return True
        for i in range(len(words)-1):
            if compare(words[i], words[i+1]) == False:
                return False
        return True
        

