# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder and not inorder:
            return None
        root= TreeNode()
        root.val= preorder[0]
        in_idx= inorder.index(root.val)
        root.left= self.buildTree(preorder[1:in_idx+1],inorder[0:in_idx] )
        root.right= self.buildTree(preorder[in_idx+1:],inorder[in_idx+1:])

        return root