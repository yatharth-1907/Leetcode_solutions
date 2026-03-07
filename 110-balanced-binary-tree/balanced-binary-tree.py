# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def balance(root:Optional[Treenode]):
            if root==None:
                return 0,True
            left,bf_l= balance(root.left)
            right,bf_r=balance(root.right)  

            bf= True if abs(left-right)<=1 else False
            count= max(left, right)
            if bf_l and bf_r and bf:
                return count+1, True
            return count+1,False
        count, bf= balance(root)
        return bf