#!/usr/bin/env python
# coding: utf-8

# In[1]:


from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.dfs(nums, [], result)
        return result
    
    def dfs(self, nums, path, result):
        
        if len(nums)==0:
            result.append(path)
        else:
            for i in range(len(nums)):
                self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], result)

        
        
if __name__ == "__main__":
    solver = Solution()
    nums = [1,2,3]
    print(solver.permute(nums))

