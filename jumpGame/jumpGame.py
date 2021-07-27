#!/usr/bin/env python
# coding: utf-8

# In[28]:


from typing import List

class Solution:
    
    def canJumpBacktracking(self, nums: List[int]) -> bool:
        return self.backtrack(0, nums)
        
    def backtrack(self, i, nums):
        if i+nums[i]>=len(nums)-1:
            return True
        else:
            # go over all steps that we can jump at index i
            for step in range(1, nums[i]+1):
                if self.backtrack(i+step, nums):
                    return True
            # if all steps at this index do not jump to the end, then try next step
            return False
    
    def canJumpGreedy(self, nums: List[int]) -> bool:
        i = 0
        while i<len(nums):
            steps = nums[i]
            if i+steps >= len(nums)-1:
                # can jump
                return True
            best_choice = 0
            max_heuristic = 0
            for choice in range(1, steps+1):
                # choose the best jumping distance
                heuristic = choice+nums[i+choice]
                if heuristic >= max_heuristic:
                    max_heuristic = heuristic
                    best_choice = choice
            if max_heuristic==0:
                return False
            # jump to this index
            i = i + best_choice
            
if __name__ == "__main__":
    nums = [2,3,1,1,4]
    solver = Solution()
    print(solver.canJumpBacktracking(nums))


# In[5]:


steps = 2
list(range(1, steps+1))


# In[ ]:




