#!/usr/bin/env python
# coding: utf-8

# In[97]:


from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        # find the pivot point using binary search
        left = 0
        right = len(nums)-1
        while left < right:
            mid = (left + right)//2
            # incase we hit the target, early stopping
            if nums[mid]==target:
                return True
            
            # handle the duplicates
            while left<right and nums[mid]==nums[left]:
                left+=1
                
            if nums[right] < nums[mid]:
                left = mid + 1
            else:
                # right is greater than middle, meaning middle is at the rotated part of the array
                right = mid
        
        # update left and right to make sure left and right bound the correct subarray that contains target
        pivot = left
        left = 0
        right = len(nums)-1
        if target>=nums[pivot] and target<=nums[right]:
            left = pivot
        else:
            right = pivot
        
        # regular binary search
        while left<=right:
            mid = (left + right)//2
            if nums[mid]==target:
                return True
            elif nums[mid]>target:
                right = mid-1
            else:
                left = mid+1
        
        return False
        
if __name__ == '__main__':
    solver = Solution()
    nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1]
    target = 2
    print(solver.search(nums, target))


# In[ ]:




