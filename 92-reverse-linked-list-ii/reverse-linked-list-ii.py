# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        
        leftprev, curr = dummy,head
        #Move left tak
        for _ in range(left -1 ):
            leftprev = curr
            curr = curr.next

        #reverse karo
        prev = None
        for _ in range(right - left + 1):
            nextNode = curr.next 
            curr.next = prev
            prev = curr
            curr = nextNode
            
        #join karo endpoints ko
        leftprev.next.next = curr
        leftprev.next = prev

        return dummy.next