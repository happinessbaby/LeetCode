# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.answer = deque()
        self.traverse(root)
        
    def traverse(self, root):
        if not root:
            return
        self.traverse(root.left)
        self.answer.appendleft(root.val)
        self.traverse(root.right)
        
        
    def next(self) -> int:
        return self.answer.pop()
    
        

    def hasNext(self) -> bool:
        if self.answer:
            return True
        return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()