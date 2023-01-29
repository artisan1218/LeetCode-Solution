#!/usr/bin/env python
# coding: utf-8

# In[15]:


# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
	def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def sameTree(p, q):
            if p==None and q==None:
                return True
            elif p==None or q==None:
                return False
            elif p.val != q.val:
                return False
            else:
                return sameTree(p.left, q.right) and sameTree(p.right, q.left)
        return sameTree(root.left, root.right)
        
        
if __name__ == '__main__':
    solver = Solution()
    
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)
    p.left.left = TreeNode(4)
    p.left.right = TreeNode(5)
    p.right.left = TreeNode(6)
    p.right.right = TreeNode(7)
    
    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(3)
    q.left.left = TreeNode(4)
    q.left.right = TreeNode(5)
    q.right.left = TreeNode(6)
    q.right.right = TreeNode(7)
    
    result = solver.isSameTreeDFS(p, q)
    print(result)


# In[ ]:




