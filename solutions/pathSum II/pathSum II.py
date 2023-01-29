#!/usr/bin/env python
# coding: utf-8

# In[1]:


from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(root, targetSum, curPath, result):
            if root!=None:
                if root.left==None and root.right==None and sum(curPath)+root.val==targetSum:
                    result.append(curPath+[root.val])
                
                if root.left!=None:
                    dfs(root.left, targetSum, curPath+[root.val], result)
                    
                if root.right!=None:
                    dfs(root.right, targetSum, curPath+[root.val], result)
                    
        result = []
        dfs(root, targetSum, [], result)
        return result
    
if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)
    
    solver = Solution()
    targetSum = 22
    print(solver.pathSum(root, targetSum))


# In[ ]:




