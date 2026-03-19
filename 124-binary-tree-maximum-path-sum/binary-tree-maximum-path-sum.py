# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxsum=-float('inf')
    def solve(self,root:Optional[TreeNode])->int:
        if root==None:
            return -float('inf')
        left= self.solve(root.left)
        right= self.solve(root.right)
        inner_loop_max= root.val+left+right
        straight_max= root.val+max(left,right)
        self.maxsum=max(self.maxsum,inner_loop_max,straight_max,root.val)
        return max(straight_max,root.val)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.solve(root)
        return self.maxsum