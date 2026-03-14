# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def size(self,root:Optional[TreeNode])-> int:
        if not root:
            return 0
        else:
            return 1+ self.size(root.left)+self.size(root.right)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        left_size= self.size(root.left)
        if k<=left_size:
            return self.kthSmallest(root.left,k)
        elif k==left_size+1:
            return root.val
        else:
            return self.kthSmallest(root.right,k-left_size-1)
        