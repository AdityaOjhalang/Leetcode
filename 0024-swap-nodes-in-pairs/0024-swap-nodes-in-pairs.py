# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        dummy = ListNode(head)
        prev,first = dummy,head
        
        while first and first.next:
            second = first.next
            nextnode = second.next

            prev.next = second
            second.next = first
            first.next = nextnode

            prev = first
            first = nextnode
        
        return dummy.next
        