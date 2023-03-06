#!/usr/bin/env python
# coding: utf-8

# In[30]:


from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class BSTIterator:
    
    def __init__(self, root: Optional[TreeNode]):
        self.result = []
        self.helper(root)
    
    def helper(self, root):
        if root:
            self.helper(root.left)
            self.result.append(root.val)
            self.helper(root.right)
        
    def next(self) -> int:
        return self.result.pop(0)

    def hasNext(self) -> bool:
        return len(self.result)>0
    
class BSTIterator2:
    
    def __init__(self, root: Optional[TreeNode]):
        self.stack = list()
        self.helper(root)
        
    def next(self) -> int:
        nextNode = self.stack.pop()
        self.helper(nextNode.right)
        return nextNode.val

    def hasNext(self) -> bool:
        return len(self.stack)>0
    
    def helper(self, node):
        while node:
            self.stack.append(node)
            node = node.left

root = TreeNode(7)
root.left = TreeNode(3)
root.right = TreeNode(15)
root.right.left = TreeNode(9)
root.right.right = TreeNode(20)

it = BSTIterator2(root)
print(it.next())
print(it.next())
print(it.hasNext())


# In[ ]:




