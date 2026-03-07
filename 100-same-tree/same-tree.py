# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p==q==None:
            return True
        if p==None or q==None:
            return False
        val=p.val==q.val
        left= self.isSameTree(p.left,q.left)
        right= self.isSameTree(p.right,q.right)

        if val and left and right :
            return True
        return False
