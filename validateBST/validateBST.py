#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isValidBSTInorderBFS(self, root: Optional[TreeNode]) -> bool:
        # BFS traversal
        # each element in level list is a 3-tuple consists of parent node value, valid range of left subtree value
        # and valid range of right subtree value
        level = [(root, (float('-inf'), root.val), (root.val, float('inf')))]
        
        while len(level)!=0:
            parent, leftRange, rightRange = level.pop()
            if parent.left!=None:
                if parent.left.val > leftRange[0] and parent.left.val < leftRange[1]:
                    # update new left and right subtree value range for left node of current parent node
                    leftLeftRange = (leftRange[0], parent.left.val)
                    leftRightRange = (parent.left.val, leftRange[1])
                    level.append((parent.left, leftLeftRange, leftRightRange))
                else:
                    return False
                        
            if parent.right!=None:
                if parent.right.val > rightRange[0] and parent.right.val < rightRange[1]:
                    # update new left and right subtree value range for right node of current parent node
                    rightLeftRange = (rightRange[0], parent.right.val)
                    rightRightRange = (parent.right.val, rightRange[1])
                    level.append((parent.right, rightLeftRange, rightRightRange))
                else:
                    return False
                
        return True
    
    def isValidBSTInorderDFS(self, root: Optional[TreeNode]) -> bool:
        if root==None:
            return True
        else:
            stack = list()
            pre = None
            
            while len(stack)!=0 or root!=None:
                # DFS, append left node all the way down
                while root != None:
                    stack.append(root)
                    root = root.left
                
                # pop one out to check
                root = stack.pop()
                # bad condition, root should be greater than pre
                if pre!=None and root.val <= pre.val:
                    return False
                
                # pre is always on the immediate left of root
                pre = root
                root = root.right
            return True
    
    def isValidBSTDFS(self, root: Optional[TreeNode]) -> bool:
        
        def helper(root, minVal, maxVal):
            if root==None:
                return True
            elif root.val <= minVal or root.val >= maxVal:
                return False
            else:
                return helper(root.left, minVal, root.val) and helper(root.right, root.val, maxVal)
        
        return helper(root, float('-inf'), float('inf'))
            
    
        
if __name__ == '__main__':
    solver = Solution()
    
    root = TreeNode(5)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)
    
    print(solver.isValidBSTInorderDFS(root))


# In[ ]:




