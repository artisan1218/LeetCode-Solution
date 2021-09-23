#!/usr/bin/env python
# coding: utf-8

# In[2]:


from typing import List

class Solution:
    def subsetsWithDupRemoveDupSubsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, cur, result, start, length):
            if len(cur)==length:
                result.append(cur.copy())
            else:
                for i in range(start, len(nums)):
                    if len(cur) + len(nums) - i + 1 >= length: # pruning
                        cur.append(nums[i])
                        backtrack(nums, cur, result, i+1, length)
                        cur.pop()
        
        result = []
        for length in range(1, len(nums)+1):
            backtrack(nums, [], result, 0, length)
        
        # remove duplicates
        result = [tuple(sorted(subset)) for subset in result]
        result = list(set(result))
        result = [list(subset) for subset in result]
        return [[]] + result
        
    def subsetsWithDupDFS(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, cur, ret, start):
            ret.append(cur.copy())
            for i in range(start, len(nums)):
                # if this is not the first element in current level, we should check
                # the element before it to make sure we do not add duplicates
                if i > start and nums[i] == nums[i-1]:
                    continue
                else:
                    cur.append(nums[i])
                    dfs(nums, cur, ret, i+1)
                    cur.pop()

        ret = []
        dfs(sorted(nums), [], ret, 0)
        return ret
    
    
if __name__ == '__main__':
    solver = Solution()
    nums = [-1,2,2]
    result = solver.subsetsWithDupDFS(nums)
    print(result)


# In[ ]:




