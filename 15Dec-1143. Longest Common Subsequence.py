class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        n1, n2 = len(text1), len(text2)     # Example: text1 = "abce"    text2 = "ace"
        bef, aft = [0]*(n2+1), [0]*(n2+1)   #            bef = [0,0,0,0]  aft = [0,0,0,0]

        for i in range(n1):                 #  (i,j)    text1[i]   text2[j]      bef         aft
            for j in range(n2):             #  ––––––   ––––––––   ––––––––   –––––––––   –––––––––
                                            #  (0,0)        a         a       [0,0,0,0]   [0,1,0,0]
                if text1[i] == text2[j]:    #  (0,1)        a         c       [0,0,0,0]   [0,1,1,1]
                    aft[j+1] = 1 + bef[j]   #  (0,2)        a         e       [0,0,0,0]   [0,1,1,1]
                                            #  (1,0)        b         a       [0,1,1,1]   [0,1,0,0]
                elif aft[j] > bef[j+1]:     #  (1,1)        b         c       [0,1,1,1]   [0,1,1,0]
                    aft[j+1] = aft[j]       #  (1,2)        b         e       [0,1,1,1]   [0,1,1,1]
                                            #  (2,0)        c         a       [0,1,1,1]   [0,1,1,1]
                                            #  (2,1)        c         c       [0,1,1,1]   [0,1,2,1]
                else:                       #  (2,2)        c         e       [0,1,1,1]   [0,1,1,2]
                    aft[j+1] = bef[j+1]     #  (3,0)        e         a       [0,1,2,2]   [0,1,1,1]
                                            #  (3,1)        e         c       [0,1,2,2]   [0,1,2,1]
            aft, bef = bef, aft             #  (3,2)        e         e       [0,1,2,2]   [0,1,2,3]
                                            #                                                    |
        return bef[-1]                      #                                                  return
