#!/usr/bin/env python
# coding: utf-8

# In[1]:


from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.dfs(nums, [], result)
        return result
    
    def dfs(self, nums, path, result):
        
        if len(nums)==0:
            result.append(path)
        else:
            unique = set()
            for i in range(len(nums)):
                if nums[i] not in unique:
                    unique.add(nums[i])
                    self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], result)

        
        
if __name__ == "__main__":
    solver = Solution()
    nums = [1,1,2]
    print(solver.permuteUnique(nums))


# In[ ]:




