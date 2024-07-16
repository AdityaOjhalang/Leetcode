# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        left_dummy = ListNode(0)
        right_dummy = ListNode(0)

        left = left_dummy
        right = right_dummy

        curr = head
        while curr:
            val = curr.val
            if val < x:
                left.next = curr
                left = left.next
            else :
                right.next = curr
                right = right.next
            curr = curr.next
        

        left.next = right_dummy.next
        #remove cycle
        
        right.next = None
        return left_dummy.next