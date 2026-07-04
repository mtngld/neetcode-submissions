# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # lets make sure p.val < q.val
        if p.val > q.val:
            p,q = q,p
        
        if p.val <= root.val and root.val <= q.val:
            return root
        elif root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        elif root.val < p.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            print(root.val, p.val, q.val)
            raise Exception("Weird!")
        