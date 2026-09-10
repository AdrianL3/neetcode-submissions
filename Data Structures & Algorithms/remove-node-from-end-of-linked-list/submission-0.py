# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #get the length of the linked list
        length = 0
        #keep a pointer to the head
        temp = head
        while temp:
            length += 1
            temp = temp.next

        #if we need to remove the head
        if n == length:
            return head.next
        
        target = length - n
        temp = head
        for i in range(target - 1):
            temp = temp.next
        
        temp.next = temp.next.next

        return head