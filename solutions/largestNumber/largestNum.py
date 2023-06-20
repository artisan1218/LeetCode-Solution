#!/usr/bin/env python
# coding: utf-8

# In[1]:


from typing import List
import functools

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        custom_key = functools.cmp_to_key(lambda a, b: 1 if b+a>a+b else -1)
        
        strNums = map(str, nums)
        trim_zeros = int(''.join(sorted(strNums, key=custom_key)))
        return str(trim_zeros)
    
solver = Solution()
print(solver.largestNumber(nums))


# In[ ]:




