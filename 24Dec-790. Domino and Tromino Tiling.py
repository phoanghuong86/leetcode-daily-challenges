class Solution:
    def numTilings(self,n:int)->int:                            # Example:  n = 5

        prev, curr, tri = 1, 1, 0                               #  n   prev  curr  tri 
                                                                # ---  ----  ----  ----
        for n in range(1,n):                                    #         1     1     0
                                                                #   2     1     2     1
            prev, curr, tri = curr, prev+curr+2*tri, prev+tri   #   3     1     2     2
                                                                #   4     1     2     4
        return curr%1000000007                                  #   5    11    24     9
                                                                #              / 
                                                                #           return
