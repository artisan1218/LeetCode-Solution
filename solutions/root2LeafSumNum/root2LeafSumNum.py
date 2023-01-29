# %%
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        def dfs(root, numSoFar):
            #nonlocal result
            numSoFar = numSoFar * 10 + root.val
            if root.left is not None:
                dfs(root.left, numSoFar)
            if root.right is not None:
                dfs(root.right, numSoFar)
            
            if root.left is None and root.right is None:
                self.result += numSoFar
        dfs(root, 0)
        return self.result

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(1)
    root.right = TreeNode(0)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(1)

    solver = Solution()
    print(solver.sumNumbers(root))

# %%



