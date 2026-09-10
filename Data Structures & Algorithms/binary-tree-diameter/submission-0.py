# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(curr):
            if not curr:
                return 0
            
            #get height of left and right subtree
            left = dfs(curr.left)
            right = dfs(curr.right)

            #the current diameter of the curr node is left + right
            self.res = max(self.res, left + right)

            #return the current max height of the subtree
            return 1 + max(left, right)

        dfs(root)
        return self.res
        