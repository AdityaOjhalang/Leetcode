# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        curr = head
        n = 1
        #n
        while curr.next:
            n += 1
            curr = curr.next
        #form a ring
        curr.next = head
        # find new tail ( n - (k%n) - 1)
        k = k%n
        if k==0:
            curr.next = None
            return head
        newt = head
        for _ in range (n-k-1):
            newt = newt.next
        
        head = newt.next
        newt.next = None

        return head

        
