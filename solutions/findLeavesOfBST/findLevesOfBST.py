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
    def findLeaves1(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        
        def dfs(root):
            if root==None:
                return 0
            else:
                height = max(dfs(root.left), dfs(root.right))
                if height >= len(result):
                    result.append([])
                result[height].append(root.val)
                return height+1
        
        dfs(root)
        return result
    
    def findLeaves2(self, root: TreeNode) -> List[List[int]]:
        leaves = []
        result = []
        
        def removeLeaves(root):
            if root!=None:
                if root.left==None and root.right==None:  # a leaf node
                    leaves.append(root.val)
                    return None # return None means we've removed the current lead node
                else:
                    # root.left and root.right will be None if it's a leat node
                    root.left = removeLeaves(root.left) 
                    root.right = removeLeaves(root.right)
                    return root # otherwise return itself, do nothing to the node
        
        while root!=None:
            root = removeLeaves(root)
            result.append(leaves)
            leaves = []
        
        return result
    
if __name__ == '__main__':
    solver = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    print(solver.findLeaves2(root))


# In[ ]:




