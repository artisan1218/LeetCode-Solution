#!/usr/bin/env python
# coding: utf-8

# In[6]:


from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def inorderTraversalDFS(self, root: Optional[TreeNode]) -> List[int]:
        
        result = []
        def dfs(root, result):
            if root==None:
                return []
            else:
                # visit left branch and add elements in the left branch first
                if root.left!=None:
                    dfs(root.left, result)
                result.append(root.val) # add root value
                # visit right branch and add elements in the right branch 
                if root.right!=None:
                    dfs(root.right, result)

        dfs(root, result)
        return result
    
    def inorderTraversalIteration(self, root: Optional[TreeNode]) -> List[int]:
        
        result = []
        stack = []
        while root!=None or len(stack)!=0:
            while root!=None:
                # explore all left branches
                stack.append(root) # not root.val but root, records the path or inorder traversal
                root = root.left
            node = stack.pop()
            result.append(node.val)
            root = node.right
        
        return result
        
        
if __name__ == '__main__':
    solver = Solution()
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    
    result = solver.inorderTraversalIteration(root)
    print(result)


# In[ ]:




