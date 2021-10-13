#!/usr/bin/env python
# coding: utf-8

# In[14]:


# Definition for a binary tree node.
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def delNodes1(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        delete = set(to_delete)
        result = []
        
        def helper(root, delete, result, parentExist):
            if root==None:
                return None
            else:
                if root.val in delete:
                    # current root is to be deleted, so return None
                    # we need to check left branch and right branch of the current root tree
                    root.left = helper(root.left, delete, result, False)
                    root.right = helper(root.right, delete, result, False)
                    return None
                else:
                    # parent not exists, either is the root of the tree, or the parents is deleted
                    # we should add it to the forest result
                    if not parentExist:
                        result.append(root)
                    # check left branch and right branch
                    root.left = helper(root.left, delete, result, True) # parent exists because root not in delete
                    root.right = helper(root.right, delete, result, True)
                    # root is kept, so return root itself instead of None
                    return root
        
        # start at root, root has no parent, so False
        helper(root, delete, result, False)
        return result
    
    def delNodes2(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        delete = set(to_delete)
        result = []
        
        def deleteNodes(root, delete, result):
            if root==None:
                return None
            else:
                # first delete nodes in left branch and right branch
                root.left = deleteNodes(root.left, delete, result)
                root.right = deleteNodes(root.right, delete, result)
                
                # we should not add root to result because it is to be deleted
                if root.val in delete:
                    if root.left != None:
                        result.append(root.left)
                    if root.right != None:
                        result.append(root.right)
                    return None
                
                return root
                
        deleteNodes(root, delete, result)
        if root.val not in delete:
            result.append(root)
            
        return result
        

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    to_delete = [3, 5]
    
    solver = Solution()
    result = solver.delNodes2(root, to_delete)
    for tree in result:
        if tree==None:
            print('null')
        else:
            print(tree.val)


# In[ ]:




