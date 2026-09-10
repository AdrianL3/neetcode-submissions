# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None:
            return True
        if root is None:
            return False

        def sameTree(first, second):
            if not first and not second:
                return True
            if not (first and second):
                return False
            else:
                if first.val != second.val:
                    return False
            
            return sameTree(first.left, second.left) and sameTree(first.right, second.right)

        def dfs(node):
            if not node:
                return False
            if node.val == subRoot.val and sameTree(node, subRoot):
                return True
                
            return dfs(node.left) or dfs(node.right)

        return dfs(root)