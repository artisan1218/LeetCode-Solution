#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Definition for a binary tree node.
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root!=None:
            left = 0
            right = 0
            if root.left!=None:
                left = self.maxDepth(root.left)
            if root.right!=None:
                right = self.maxDepth(root.right)

            return 1 + max(left, right)
        else:
            return 0
        
    def maxDepthOneline(self, root: Optional[TreeNode]) -> int:
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) if root!=None else 0
    
        
        
if __name__ == '__main__':
    solver = Solution()
    
    p = TreeNode(3)
    p.left = TreeNode(9)
    p.right = TreeNode(20)
    p.right.left = TreeNode(15)
    p.right.right = TreeNode(17)
    
    result = solver.maxDepthOneline(p)
    print(result)


# In[ ]:




