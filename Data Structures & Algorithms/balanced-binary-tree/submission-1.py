# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getHeight(self, root: Optional[TreeNode]) -> tuple(bool, int):
        if root is None:
            return (True, 0)
        left_result = self.getHeight(root.left)
        right_result = self.getHeight(root.right)
        is_balanced = abs(left_result[1] - right_result[1]) <= 1 and left_result[0] and right_result[0]
        height = 1 + max(left_result[1], right_result[1])
        return is_balanced, height


    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        root_result = self.getHeight(root)
        return root_result[0]