# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.d = defaultdict(list)

    def bfs(self, root, level):
        if root is None:
            return
        self.d[level].append(root.val)
        self.bfs(root.left, level + 1)
        self.bfs(root.right, level + 1)
        



    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.bfs(root, 0)
        result = []
        print(self.d)
        for x in range(len(self.d.keys())):
            result.append(self.d[x])
        return result

