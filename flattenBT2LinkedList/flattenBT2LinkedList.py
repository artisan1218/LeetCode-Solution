#!/usr/bin/env python
# coding: utf-8

# In[8]:


# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    '''
    The brute force solution, what we do is simply get the preorder traversal result and store each node as reference
    in a list. Then point the current node in list to next node in list for each node
    '''
    def flattenBruteForce(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def preorder(root):
            if root!=None:
                result.append(root)
                preorder(root.left)
                preorder(root.right)
        
        result = list()
        preorder(root)
        
        # cannot reassign root directly because root=xx is the reference to local variable, not the actual root
        for i in range(len(result)-1):
            result[i].left = None
            result[i].right = result[i+1]
            
   
    '''
    The idea is to find the predecessor of preorder traversal for each node, insert the left subtree to the right
    subtree and repeat this process iteratively
    
     For tree:
        1
       / \
      2   5
     / \   \
    3   4   6
    
    We first insert left subtree of node 1 to right subtree
        1
         \    \
          2    5
         / \    \
        3   4    6
        
    Then concat right subtree to the end
        1
         \    
          2    
         / \    
        3   4   
             \
              5
               \
                6
    
    Then we do the same for the left subtree of node 2, etc.
    '''
    def flattenIteration(self, root: Optional[TreeNode]) -> None:
        cur = root
        while cur!=None:
            if cur.left!=None:
                nxt = cur.left
                pre = cur.left
                while pre.right!=None:
                    pre = pre.right
                pre.right = cur.right
                cur.right = nxt
                cur.left = None
            else:
                cur = cur.right
        
    '''
    The idea is from preorder traversal where we simply visit nodes in pre-order and change the pointer to next node
    iteratively. However, if we visit the nodes in pre-order and change the reference of current node, we will 
    lose reference to the unvisited nodes. Instead, we can do preorder traversal in reverse order to avoid this problem,
    we therefore can make sure that each visited node is already updated.
    
    For tree:
        1
       / \
      2   5
     / \   \
    3   4   6
    
    We visit in reversed pre-order, which is 6, 5, 4, 3, 2, 1
    Then we update the right child of each node in order:
     6->5, 4, 3, 2, 1
     
     6->5->4, 3, 2, 1
     
     6->5->4->3, 2, 1
     
     6->5->4->3->2, 1
     
     6->5->4->3->2->1
    
    '''    
    def flattenReversedPreorder(self, root: Optional[TreeNode]) -> None:
        self.pre = None
        def helper(root):
            if root!=None:
                pre = helper(root.right)
                pre = helper(root.left)
                
                root.right = self.pre # pre starts with None, which means the right child of last node is None
                root.left = None
                self.pre = root
                
        helper(root)
        
    '''
    The idea is to use a stack to store the nodes in preorder, then redirecting each node to the next node, which
    is the last node in stack
    '''
    def flattenStack(self, root: Optional[TreeNode]) -> None:
        if root!=None:
            stack = [root]
            while len(stack)!=0:
                curr = stack.pop()
                
                if curr.right!=None:
                    stack.append(curr.right)
                if curr.left!=None:
                    stack.append(curr.left)
                    
                if len(stack)!=0:
                    curr.right = stack[-1]
                    
                curr.left = None
        
        
    
if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(6)
    
    solver = Solution()
    solver.flattenStack(root)
    
    while root!=None:
        print(root.val)
        root = root.right


# In[ ]:




