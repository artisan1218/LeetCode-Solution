#!/usr/bin/env python
# coding: utf-8

# In[3]:


from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left + right)//2
            left_nei = nums[mid-1] if mid-1 >= 0 else float('-inf')
            right_nei = nums[mid+1] if mid+1 <= len(nums)-1 else float('-inf')
            
            if nums[mid] > right_nei and nums[mid] > left_nei:
                return mid
            elif nums[mid] < right_nei:
                # there must exist a peak element on the right
                # even though there also might be peak elements on the left
                left = mid+1
            else:
                right = mid-1
    
    
solver = Solution()
nums = [1,2,1,3,5,6,4]
# nums = [1,2,3,4,5]
print(solver.findPeakElement(nums))


# In[ ]:




