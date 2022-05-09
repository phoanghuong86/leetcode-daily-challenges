# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: List[NestedInteger]):
        self.gen = self._recur(nestedList)
        self.next_val = next(self.gen, None)

    def _recur(self, lst: List[NestedInteger]):
        for el in lst:
            if el.isInteger():
                yield el.getInteger()
            else:
                yield from self._recur(el.getList())

    def next(self) -> int:
        ans = self.next_val
        self.next_val = next(self.gen, None) 
        return ans
        
    def hasNext(self) -> bool:
        return self.next_val is not None
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
