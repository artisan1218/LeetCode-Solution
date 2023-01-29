#!/usr/bin/env python
# coding: utf-8

# In[2]:


from typing import List

class Solution:
    def findMinRecurssion(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        while right > left:
            mid = (left+right)//2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] == nums[right]:
                return min(self.findMin(nums[mid:right]), 
                           self.findMin(nums[left:mid+1]))
            else:
                right = mid
        return nums[left]
    
    
    def findMinIterative(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        while right > left:
            mid = (left+right)//2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] == nums[right]:
                right-=1
            else:
                right = mid
        return nums[left]
    
    
if __name__ == "__main__":
    solver = Solution()
    # nums = [1,1]
    # nums = [3,1,3,3,3]
    nums = [3,3,3,1,3]
    # nums = [3,3,1,3]
    # nums = [3,3,4,0,1,2,3,3,3]
    print(solver.findMinIterative(nums))


# In[ ]:




