class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        d = defaultdict(list)
        
        l = [[root,[0,0]]]
        # print(d)
        i = 0
        while l:
            d1 = defaultdict(list)
            temp = []
            while l:
                a = l.pop()
                d1[a[1][1]].append(a[0].val)
            
                if a[0].left:
                    temp.append([a[0].left,[a[1][0]+1,a[1][1]-1]])
                if a[0].right:
                    temp.append([a[0].right,[a[1][0]+1,a[1][1]+1]])
            l = temp
            for i in d1:
                d[i] = d[i]+sorted(d1[i])
        
        res = []
        i = min(d.keys())
        
        while len(d) != 0:
            if i in d:
                res.append(d[i])
                del d[i]
            i += 1
        return res
