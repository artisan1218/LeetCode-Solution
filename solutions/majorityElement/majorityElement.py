#!/usr/bin/env python
# coding: utf-8

# In[2]:


from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        result = 0
        for num in nums:
            if count==0:
                result = num
                count = 1
            else:
                if num==result:
                    count+=1
                else:
                    count-=1
        return result
    
solver = Solution()
nums = [2,2,1,1,1,2,2]
print(solver.majorityElement(nums))


# In[ ]:




