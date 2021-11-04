#!/usr/bin/env python
# coding: utf-8

# In[7]:


# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        if root==None:
            return True
        else:
            leftDepth = self.getDepth(root.left) # get the depth of current left subtree
            rightDepth = self.getDepth(root.right) # get the depth of current right subtree
            if abs(leftDepth - rightDepth) > 1:
                return False
            else:
                # keep checking left subtree and right subtree
                return self.isBalanced(root.left) and self.isBalanced(root.right)
        
    def getDepth(self, root):
        if root==None:
            return 0
        else:
            left = self.getDepth(root.left) + 1
            right = self.getDepth(root.right) + 1
            return max(left, right)
        
        
if __name__ == '__main__':
    solver = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    
    result = solver.isBalanced(root)
    print(result)


# In[ ]:




