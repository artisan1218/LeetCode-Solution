#!/usr/bin/env python
# coding: utf-8

# In[27]:


from typing import List

class Solution:
    def robRecursion(self, nums: List[int]) -> int:
        mem = dict()
        def dfs(nums, i, mem):
            if i in mem:
                return mem[i]
            else:
                if i>=len(nums):
                    return 0
                else:
                    option1 = nums[i] + dfs(nums, i+2, mem) # rob current house and rob i+2
                    option2 = dfs(nums, i+1, mem) # skip this one and rob i+1

                    mem[i] = max(option1, option2)
                    return mem[i] 
        return dfs(nums, 0, mem)
    
    def robDP(self, nums: List[int]) -> int:
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])
        
        for i in range(2, len(nums)):
            # for each num at i, we found the max value of i-1 or i-2 + nums[i]
            # dp[i-1] means rob the previous one, so that we cannot rob the current
            # dp[i-2] + num means rob the current one and the one before previous one
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        
        return dp[-1]
    
    def robDP2(self, nums: List[int]) -> int:
        pre = 0
        cur = 0
        for num in nums:
            # pre + num means rob the current one and the one before the previous one
            # cur means rob the previous one, so we cannot rob current one(num) or the one before previous one(pre)
            pre, cur = cur, max(pre+num, cur)
        
        return cur
            
        
if __name__ == '__main__':
    solver = Solution()
    nums = [2,7,3,1,9]
    print(solver.robDP2(nums))

