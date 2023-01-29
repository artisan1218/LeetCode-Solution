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
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root!=None:
            result = list()
            queue = [root]
            while len(queue)!=0:
                levelLen = len(queue)
                level = list()
                for i in range(levelLen):
                    node = queue.pop(0)
                    level.append(node.val)
                    if node.left!=None:
                        queue.append(node.left)
                    if node.right!=None:
                        queue.append(node.right)
                result.append(level)
            return result[::-1]
        else:
            return []

if __name__ == '__main__':
    solver = Solution()
    
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(2)
    p.left.left = TreeNode(3)
    p.left.right = TreeNode(4)
    p.right.left = TreeNode(4)
    p.right.right = TreeNode(3)
    
    result = solver.levelOrderBottom(p)
    print(result)


# In[ ]:




