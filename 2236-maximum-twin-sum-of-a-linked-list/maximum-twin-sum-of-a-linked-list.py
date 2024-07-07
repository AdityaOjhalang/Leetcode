# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        def findMid(head: Optional[ListNode]):
            slow = head
            fast = head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        def RevLinkedList(head: Optional[ListNode]):
            prev = None
            curr = head
            while curr:
                nextNode = curr.next
                curr.next = prev
                prev = curr
                curr = nextNode
            return prev
        mid = findMid(head)
        second = RevLinkedList(mid)

        first = head
        res = 0
        while second:
            currsum = first.val + second.val
            res = max(res,currsum)

            first = first.next
            second = second.next
        return res

