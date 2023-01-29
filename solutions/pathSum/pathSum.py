#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, result, curSum):
            if root!=None:
                if root.left==None and root.right==None:
                    result.add(curSum + root.val)
                
                if root.left!=None:
                    dfs(root.left, result, curSum + root.val)

                if root.right!=None:
                    dfs(root.right, result, curSum + root.val)
        
        result = set()
        dfs(root, result, 0)
        return targetSum in result          
        
    def hasPathSum2(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, result, target):
            if root!=None:
                if root.left==None and root.right==None and target==root.val:
                    result.append(True)
                
                if root.left!=None:
                    dfs(root.left, result, target - root.val)

                if root.right!=None:
                    dfs(root.right, result, target - root.val)
        
        result = list()
        dfs(root, result, targetSum)
        return any(result)
    
    def hasPathSum3(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, curSum):
            result = False
            if root!=None:
                if root.left==None and root.right==None and curSum + root.val == targetSum:
                    return True
                
                if root.left!=None:
                    result = result or dfs(root.left, curSum + root.val)

                if root.right!=None:
                    result = result or dfs(root.right, curSum + root.val)
                
                return result
        
        return dfs(root, 0)
    
    def hasPathSum4(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root==None:
            return False
        elif root.left==None and root.right==None and targetSum==root.val:
            return True
        else:
            left = self.hasPathSum4(root.left, targetSum-root.val)
            right = self.hasPathSum4(root.right, targetSum-root.val)
            return left or right
        
    
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
    print(solver.hasPathSum4(root, targetSum))


# In[ ]:




