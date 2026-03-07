# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def diameter(root:Optional[TreeNode]):
            dia,count=0,0
            if root==None:
                return 0,0
            elif root.left==None and root.right==None:
                return 1,0
            count_l,dia_l= diameter(root.left)
            count_r,dia_r= diameter(root.right)
            count= max(count_l,count_r)
            dia= max(dia_l,dia_r,count_l+count_r)
            return count+1, dia
        count, dia= diameter(root)
        return dia
