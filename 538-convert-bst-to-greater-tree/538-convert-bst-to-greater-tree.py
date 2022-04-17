# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.partial_sum = 0
        
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        self.convertBST(root.right)
        root.val+=self.partial_sum
        self.partial_sum=root.val
        self.convertBST(root.left)
        return root

        