# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        leftdummy,rightdummy = ListNode(),ListNode()
        left,right = leftdummy,rightdummy
        curr = head
        while curr:
            if curr.val < x:
                left.next = curr
                left = left.next
            else:
                right.next = curr
                right = right.next
            curr = curr.next
        
        left.next = rightdummy.next
        #right pointer might still pe pointing somewhere in the original list put it none and eliminate cycle
        right.next = None
        return leftdummy.next