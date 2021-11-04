#!/usr/bin/env python
# coding: utf-8

# In[18]:


from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def minDepth1(self, root: Optional[TreeNode]) -> int:
        
        def depth(root, curDepth, depthList):
            if root.left==None and root.right==None: # this is a leaf node
                depthList[0] = min(depthList[0], curDepth)
            else:
                if root.left!=None:
                    left = depth(root.left, curDepth+1, depthList)
                if root.right!=None:
                    right = depth(root.right, curDepth+1, depthList)
        
        if root==None:
            return 0
        else:
            depthList = [float('inf')]
            depth(root, 1, depthList)
            return depthList[0]
    
    def minDepth2(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        else:
            if root.left==None:
                return self.minDepth2(root.right) + 1 # left node is none, only counting right node
            elif root.right==None:
                return self.minDepth2(root.left) + 1 # right node is none, only counting left node
            else:
                # counting both and take minimal if both left and right are non-null
                left = self.minDepth2(root.left) + 1
                right = self.minDepth2(root.right) + 1
                return min(left, right)
    

if __name__ == '__main__':
    solver = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    
    print(solver.minDepth2(root))


# In[ ]:





# In[ ]:




