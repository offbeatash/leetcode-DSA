# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        pos = {v:i for i, v in enumerate(inorder)}
        pre_idx = 0

        def dfs(left,right):
            nonlocal pre_idx

            if left>right:
                return None

            val = preorder[pre_idx]
            pre_idx +=1

            root = TreeNode(val)
            mid = pos[val]

            root.left = dfs(left, mid-1)
            root.right = dfs(mid+1,right)

            return root

        return dfs(0, len(inorder)-1)  