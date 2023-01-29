#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Definition for a binary tree node.
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        if len(preorder)==0 or len(inorder)==0:
            return None
        else:
            # root is always the first element in preorder traversal
            rootVal = preorder[0]
            root = TreeNode(rootVal)
            # find the index of root at inorder list because to get the left subtree and right subtree
            inorderRootIdx = inorder.index(rootVal)
            
            # for the left subtree, we know the possible range are all the values before the rootIdx and after 1
            # because we've used the first element, which is the current root
            # for the right subtree, we know the possible range are all the values after the rootIdx in inorder traversal
            root.left = self.buildTree(preorder[1:inorderRootIdx+1], inorder[0:inorderRootIdx])
            root.right = self.buildTree(preorder[inorderRootIdx+1:], inorder[inorderRootIdx+1:])
            return root            
        
if __name__ == '__main__':
    solver = Solution()
    
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    
    result = solver.buildTree(preorder, inorder)


# In[ ]:




