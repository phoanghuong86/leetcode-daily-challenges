# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        n = len(nums)
        if n == 1:
            return TreeNode(nums[0])

        def build(start: int, end: int) -> Optional[TreeNode]:
            if start <= end:
                mid = (start + end) // 2
                return TreeNode(nums[mid], build(start, mid - 1), build(mid + 1, end))
            return None

        return build(0, n - 1)
