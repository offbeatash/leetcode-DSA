class Solution:
    def hasPathSum(self, root, targetSum):
        if not root:
            return False

        stack = [(root, targetSum)]

        while stack:
            node, remaining = stack.pop()
            remaining -= node.val

            if node.left is None and node.right is None:
                if remaining == 0:
                    return True

            if node.left:
                stack.append((node.left, remaining))

            if node.right:
                stack.append((node.right, remaining))

        return False