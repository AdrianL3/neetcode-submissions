# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # step 1: find length of the list
        length, temp = 0, head
        while temp:
            length += 1
            temp = temp.next
        
        target = length - n
        if target == 0:
            return head.next
        
        newTemp = head
        for i in range(target - 1):
            newTemp = newTemp.next
        
        newTemp.next = newTemp.next.next

        return head