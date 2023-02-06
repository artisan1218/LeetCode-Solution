#!/usr/bin/env python
# coding: utf-8

# In[11]:


from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, right = 0, 0
        max_num = 0
        while right<len(nums):
            if nums[right]==1:
                right+=1
            else:
                if k>0:
                    k-=1 # flip
                    right+=1
                else:
                    # used all flips and current right is 0
                    # we need to move left pointer to left
                    left+=1
                    if nums[left]==0:
                        k+=1 # reclaim one flip chance
            max_num = max(max_num, right-left)
        return max_num

solver = Solution()
#nums = [1,1,1,0,0,0,1,1,1,1,0]
nums = [0,0,0,1]
k = 3
print(solver.longestOnes(nums, k))


# In[ ]:




