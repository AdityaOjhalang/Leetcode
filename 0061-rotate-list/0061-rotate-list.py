# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head
        #finding the length of linkedlist
        n = 1
        curr = head
        while curr and curr.next: # curr.next will make sure curr is not null when we want to create cycle
            curr = curr.next
            n+=1
        #creating a loop
        curr.next = head
        #effective rotations 
        k = k%n
        if k == 0:
            return head 
        #go to the new tail 
        tail = head
        for _ in range(n-k-1): 
            tail = tail.next
        #new head and tail config
        newhead = tail.next
        tail.next = None

        return newhead

        
        