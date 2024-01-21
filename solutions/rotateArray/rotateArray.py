#!/usr/bin/env python
# coding: utf-8

# In[3]:


from typing import List

class Solution:
    def rotatePopAndInsertOneByOne(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            transfer = nums.pop(-1)
            nums.insert(0, transfer)
        
    def rotateCut(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k  = k % len(nums) # if k is longer than length of nums, take the remainder of it
        end = nums[:len(nums)-k] # get the part that will be attached to the end
        del nums[:len(nums)-k] # remove the part from front
        nums.extend(end) # attach to end
    
    def rotateO1Space(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k  = k % len(nums)
        def reverseSubList(nums, left, right):
            for i in range((right-left)//2):
                nums[left+i], nums[right-i-1] = nums[right-i-1], nums[left+i]
            
        reverseSubList(nums, 0, len(nums)-k)
        reverseSubList(nums, len(nums)-k, len(nums))
        nums.reverse()
        
if __name__ == '__main__':
    nums = [1,2,3,4,5,6,7]
    k = 3
    solver = Solution()
    solver.rotateO1Space(nums, k)
    print(nums)


# In[ ]:




