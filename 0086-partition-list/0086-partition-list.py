# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        leftd,rightd = ListNode(0),ListNode(0)
        left,right = leftd,rightd
        curr = head
        while curr:
            val = curr.val
            if val < x:
                left.next = curr
                left = left.next     
            else:
                right.next = curr
                right = right.next
            curr = curr.next
        left.next = rightd.next
        right.next = None
        return leftd.next
