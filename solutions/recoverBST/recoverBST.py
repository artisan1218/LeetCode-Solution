#!/usr/bin/env python
# coding: utf-8

# In[87]:


# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.start = None
        self.end = None
        self.pre = None
        
        def dfs(root):
            if root!=None:
                dfs(root.left)
                
                if self.pre == None:
                    self.pre = root
                else:
                    # in-order traversal of BST will explore nodes in ascending order
                    if self.pre.val > root.val:
                        # previous node is bigger than current node, this is a mistake
                        # end might be changed, but start is fixed
                        self.end = root
                        if self.start == None:
                            self.start = self.pre # only assigned once
                    self.pre = root
                
                dfs(root.right)
            else:
                return
        
        dfs(root)
        self.start.val, self.end.val = self.end.val, self.start.val
        
if __name__ == '__main__':
    solver = Solution()
    
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.left.right = TreeNode(2)
    
    solver.recoverTree(root)       


# In[ ]:




