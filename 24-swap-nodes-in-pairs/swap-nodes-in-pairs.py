# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        prev , first = dummy , head

        while first and first.next:
            #save nodes so that we have reference 
            second = first.next
            nextNode = first.next.next
            #make changes
            first.next = nextNode
            second.next = first
            prev.next = second
            #update
            prev = first
            first = first.next

        return dummy.next

