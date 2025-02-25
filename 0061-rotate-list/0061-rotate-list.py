# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head  or k == 0:
            return head
        curr = head
        n = 1
        while curr and curr.next: #curr.next will make sure that curr is not null
            curr = curr.next
            n+=1
        #effective rotations (value of k)
        k = k%n # for k > n 
        if k == 0:
            return head
        
        #make a cycle
        curr.next = head
        tail = head
        for _ in range(n-k-1):
            tail = tail.next
        
        #break cycle
        newhead = tail.next
        tail.next = None

        return newhead
       
        
