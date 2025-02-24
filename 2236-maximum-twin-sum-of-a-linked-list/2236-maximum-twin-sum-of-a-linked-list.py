# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        def findmid(head: Optional[ListNode]):
            slow = fast = head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow 
        def rev(head: Optional[ListNode]):
            prev = None
            curr = head
            while curr:
                nextnode = curr.next
                curr.next = prev
                prev = curr
                curr = nextnode
            return prev
        mid = findmid(head)
        fast = rev(mid)
        slow = head
        res = 0
        while fast:
            res = max(res,fast.val+slow.val)
            fast = fast.next
            slow = slow.next
        return res

