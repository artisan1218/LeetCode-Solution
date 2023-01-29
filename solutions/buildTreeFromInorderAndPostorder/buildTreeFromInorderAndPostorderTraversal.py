#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Definition for a binary tree node.
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(inorder)==0 or len(postorder)==0:
            return None
        else:
            # we can get root from the last element in postorder
            root = TreeNode(postorder[-1])
            
            # then find the root index in the inorder list, left sublist will be elements on the left subtree
            # right sublist will be on the right substree
            inorderRootIdx = inorder.index(postorder[-1])
            
            # split the inorder list at the root index, do the same thing to postorder except for the last element,
            # which is the root value, we skip that because root is already used
            root.left = self.buildTree(inorder[0:inorderRootIdx], postorder[0:inorderRootIdx])
            root.right = self.buildTree(inorder[inorderRootIdx+1:], postorder[inorderRootIdx:-1])
            return root
    
        
if __name__ == '__main__':
    solver = Solution()
    
    inorder = [1,2]
    postorder = [2,1]
    
    result = solver.buildTree(inorder, postorder)


# In[ ]:




