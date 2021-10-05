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
    def sortedArrayToBST1(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums)==0:
            return None
        else:
            # find a middle point
            mid = len(nums)//2
            # make middle point at the root 
            root = TreeNode(nums[mid])
            root.left = self.sortedArrayToBST1(nums[0:mid])
            root.right = self.sortedArrayToBST1(nums[mid+1:])
            return root
        
    def sortedArrayToBST2(self, nums: List[int]) -> Optional[TreeNode]:
        
        def helper(nums, low, high):
            if low > high:
                return None
            else:
                mid = (high+low)//2
                root = TreeNode(nums[mid])
                root.left = helper(nums, low, mid-1)
                root.right= helper(nums, mid+1, high)
                return root
        return helper(nums, 0, len(nums)-1)
        
if __name__ == '__main__':
    nums = [-10,-3,0,5,9]
    solver = Solution()
    tree = solver.sortedArrayToBST2(nums)


# In[ ]:




