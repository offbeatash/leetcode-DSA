# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxed):
            if not node :
                return 0

            count = 0
            if node.val >= maxed:
                count = 1
            
            maxed = max(maxed, node.val)

            count += dfs(node.left, maxed)
            count += dfs(node.right, maxed)

            return count

        return dfs(root, root.val)