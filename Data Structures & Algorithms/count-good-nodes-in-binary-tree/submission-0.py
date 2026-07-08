# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root: TreeNode, max_val: int):
        if root is None:
            return 0
        
        if root.val >= max_val:
            return (1 + 
                self.dfs(root.left, root.val) + 
                self.dfs(root.right, root.val))
        else:
            return self.dfs(root.left, max_val) + self.dfs(root.right, max_val)
        

    
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root, -1000)