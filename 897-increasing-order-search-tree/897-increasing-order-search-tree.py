# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        res = self.tree = TreeNode()
        def traverse(root):
            if not root:
                return
            traverse(root.left)
            self.tree.right = TreeNode(root.val)
            self.tree=self.tree.right
            traverse(root.right)
        traverse(root)
        return res.right
        