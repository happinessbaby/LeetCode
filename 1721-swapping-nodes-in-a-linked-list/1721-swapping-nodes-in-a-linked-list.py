# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count=0
        temp1 = head
        first_elem = 0
        while temp1:
            count+=1
            if count==k:
                first_elem = temp1.val
            temp1=temp1.next
        k_end = count-k+1
        count = 0
        second_elem = 0
        temp2 = head
        while temp2:
            count+=1
            if count==k_end:
                second_elem = temp2.val
            temp2=temp2.next
        temp3 = head
        count = 0
        while head:
            count+=1
            if count==k:
                head.val = second_elem
            elif count == k_end:
                head.val = first_elem
            head=head.next
        return temp3
                
                
        
                