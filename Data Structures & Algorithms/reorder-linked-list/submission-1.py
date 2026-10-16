# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # split the list in half
        second = slow.next
        slow.next = None
        prev = None

        while second:
            nextNode = second.next
            second.next = prev
            prev = second
            second = nextNode
        
        first = head
        second = prev

        # now do the alternating
        while second:
            firstNext = first.next
            secondNext = second.next

            first.next = second
            second.next = firstNext

            first = firstNext
            second = secondNext
