# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #BFS to do level-be-level traversla
        res = []
        q = deque([root])

        while q:
            rightSide = None
            qLen = len(q)

            for i in range(qLen):
                node = q.popleft()
                if node:
                    rightSide = node
                    #append left to right, so that the right node will be the last node to be assigned
                    q.append(node.left)
                    q.append(node.right)
            #append the rightmost element of the level
            if rightSide:
                res.append(rightSide.val)
            
        return res