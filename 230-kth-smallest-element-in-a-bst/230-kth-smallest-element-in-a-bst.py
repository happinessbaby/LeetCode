# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = k
        self.answer = None
        def traverse(root):
            if not root:
                return
            traverse(root.left)
            self.count-=1
            if self.count==0:
                self.answer = root.val
                return
            traverse(root.right)
        traverse(root)
        return self.answer