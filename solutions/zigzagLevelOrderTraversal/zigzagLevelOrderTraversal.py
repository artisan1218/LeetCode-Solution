#!/usr/bin/env python
# coding: utf-8

# In[17]:


# Definition for a binary tree node.
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root!=None:
            result = list()
            level = [root]
            result.append([node.val for node in level])
            l2r = False
            while len(level)!=0:
                nextLevel = list()
                for node in level:
                    if node.left!=None:
                        nextLevel.append(node.left)
                    if node.right!=None:
                        nextLevel.append(node.right)
                if l2r:
                    result.append([node.val for node in nextLevel])
                else:
                    result.append([node.val for node in reversed(nextLevel)])
                level = nextLevel
                l2r = not l2r
                
            return result[:-1]
        else:
            return []
        
        
        
if __name__ == '__main__':
    solver = Solution()
    
    p = TreeNode(3)
    p.left = TreeNode(9)
    p.right = TreeNode(20)
    p.right.left = TreeNode(15)
    p.right.right = TreeNode(17)
    
    result = solver.zigzagLevelOrder(p)
    print(result)


# In[3]:


nextLevel = [1,2,3] 
nextLevel[::-1]


# In[ ]:




