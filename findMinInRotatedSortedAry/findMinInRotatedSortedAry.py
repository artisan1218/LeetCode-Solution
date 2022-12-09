#!/usr/bin/env python
# coding: utf-8

# In[2]:


from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        while right > left:
            mid = (left+right)//2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
            
        return nums[left]
    
if __name__ == '__main__':
    solver = Solution()
    nums = [4,5,6,7,0,1,2]
    # nums = [5,6,7,8,9]
    print(solver.findMin(nums))


# In[ ]:




