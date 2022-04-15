# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        def traverse(root):
            if not root:
                return
            elif root.val>high:
                return traverse(root.left)
            elif root.val<low:
                return traverse(root.right)
            else:
                root.left = traverse(root.left)
                root.right = traverse(root.right)
                return root
        return traverse(root)
        