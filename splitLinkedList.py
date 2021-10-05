from collections import deque

# Definition for singly-linked list.
 class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:


    def __init__(self):
        self.head = None

    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        answer = deque()
        while head:
            self.insert_head(head.val)
            head = head.next
            length +=1
        (d, r) = divmod(length, k)
        x = k - length
        if x > 0: #insert [] when k>length
            y = x
            while x>0:
                self.insert_head(str([])[1:-1])
                x -= 1
        else:
            y = 0
        a, m, n =0, 0, 0
        while n < length+y:
            if a >= k-r-y:
                m = 1
            i = 0
            prev = None
            curr = self.head
            while i<m+d: #reverse sublist
                nex = curr.next
                curr.next = prev
                prev=curr
                curr = nex
                i+=1
            answer.appendleft(prev)
            self.head = curr
            n+=d+m
            a+=1
        return answer


    def insert_head(self, h):
        new_n = ListNode(h)
        new_n.next = self.head
        self.head = new_n


s= Solution()
print(s.splitListToParts([1,2,3], k = 5))
