#!/usr/bin/env python
# coding: utf-8

# In[19]:


from typing import List

class Solution:
    def minDifferenceBruteForce(self, nums: List[int]) -> int:
        if len(nums)>4:
            left = 0
            right = len(nums)-1
            nums.sort()
            
            lll = nums[right] - nums[left+3] # cut 3 smallest elements
            rrr = nums[right-3] - nums[left] # cut 3 biggest elements
            llr = nums[right-1] - nums[left+2] # cut 2 smallest and 1 biggest
            lrr = nums[right-2] - nums[left+1] # cut 1 smallest and 2 biggest
            
            return min(lll, rrr, llr, lrr)
        else:
            return 0
    
    def minDifferenceBacktrack(self, nums: List[int]) -> int:
        
        def backtrack(nums, remainingNum, left, right):
            if remainingNum!=0:
                cutFromLeft = backtrack(nums, remainingNum-1, left+1, right)
                cutFromRight = backtrack(nums, remainingNum-1, left, right-1)
                return min(cutFromLeft, cutFromRight)
            else:
                return nums[right]-nums[left]
            
        if len(nums)>4:
            nums.sort()
            return backtrack(nums, 3, 0, len(nums)-1)
        else:
            return 0
        
        
if __name__ == '__main__':
    solver = Solution()
    nums = [9,48,92,48,81,31]
    print(solver.minDifferenceBacktrack(nums))

