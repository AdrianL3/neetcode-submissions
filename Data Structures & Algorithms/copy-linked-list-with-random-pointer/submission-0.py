"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        newNodes = {}
        newNodes[None] = None

        curr = head

        while curr:
            copy = Node(curr.val)

            newNodes[curr] = copy

            curr = curr.next

        result = newNodes[head]
        currCopy = newNodes[head]

        while currCopy:
            currCopy.next = newNodes[head.next]
            currCopy.random = newNodes[head.random]
            head= head.next
            currCopy = currCopy.next

        return result