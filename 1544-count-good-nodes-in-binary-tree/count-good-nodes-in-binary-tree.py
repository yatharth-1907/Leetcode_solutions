# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def goodnode(root:TreeNode, m= None):
            if not root:
                return 0
            if m==None:
                return 1 +goodnode(root.left,root.val)+goodnode(root.right,root.val)
            if root.val<m:
                return goodnode(root.left,m)+goodnode(root.right,m)
            if root.val>=m:
                return 1+ goodnode(root.left,root.val)+goodnode(root.right,root.val)
        return goodnode(root,None)