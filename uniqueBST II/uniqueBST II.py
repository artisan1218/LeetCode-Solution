#!/usr/bin/env python
# coding: utf-8

# In[19]:


# Definition for a binary tree node.
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        nList = list(range(1, n+1))
        return self.helper(nList)
    
    def helper(self, nList):
        # if all values are used, return an empty branch of [None], not a None value!
        if len(nList)==0:
            return [None]
        else:
            # result that holds all branches under current root
            result = []
            for i in range(len(nList)):
                leftBranches = self.helper(nList[:i]) # get all left branches
                rightBranches = self.helper(nList[i+1:]) # get all right branches
                
                # go through each combination of left and right branch
                for leftBranch in leftBranches:
                    for rightBranch in rightBranches:
                        # construct a binary tree with current value as root 
                        root = TreeNode(nList[i])
                        root.left = leftBranch
                        root.right = rightBranch
                        
                        result.append(root)
            return result
        
        
if __name__ == '__main__':
    solver = Solution()
    n = 3
    result = solver.generateTrees(n)
    print(result)    
    


# In[ ]:




