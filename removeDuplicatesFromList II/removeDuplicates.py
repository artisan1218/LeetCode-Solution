#!/usr/bin/env python
# coding: utf-8

# In[59]:


from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        duplicates = 2
        modCursor = 0
        checkCursor = 0
        
        while checkCursor<len(nums):
            # for the beginning n words, simply increment the modCursor
            if modCursor < duplicates:
                modCursor+=1
            # this means we've met a new value, it's time to update the elements at modCursor
            elif nums[checkCursor] > nums[modCursor-duplicates]:
                nums[modCursor] = nums[checkCursor]
                modCursor+=1
            checkCursor+=1
        
        return modCursor
        
if __name__ == '__main__':
    solver = Solution()
    nums = [1,1,1,2,2,3]
    k = solver.removeDuplicates(nums)
    print('first K elements:'.ljust(17), nums[:k])
    print('all elements:'.ljust(17), nums)


# In[ ]:




