#!/usr/bin/env python
# coding: utf-8

# In[4]:


from typing import List
import math

class Solution:
    def maxProductCountNegNum(self, nums: List[int]) -> int:
        def maxProductInAryWithoutZero(nums):
            if len(nums) == 1:
                return nums[0]
            else:
                firstNegIndex = -1
                lastNegIndex = -1
                negCount = 0
                for i, n in enumerate(nums):
                    if n < 0:
                        negCount += 1
                        if firstNegIndex == -1:
                            firstNegIndex = i
                        lastNegIndex = i
                if negCount%2 == 0:
                    return math.prod(nums)
                else:
                    # odd number of negative number, then we only care about the first and last neg number
                    # we can either include the first one and exclude the last one
                    # or exclude the first one and include the last one
                    return max(math.prod(nums[0:lastNegIndex]), math.prod(nums[firstNegIndex+1:]))
        
        # split by 0
        subary = []
        result = max(nums)
        for i, n in enumerate(nums):
            if n==0:
                if len(subary)!=0:
                    result = max(result, maxProductInAryWithoutZero(subary.copy()))
                    subary = []
            else:
                subary.append(n)
                if i==len(nums)-1:
                    result = max(result, maxProductInAryWithoutZero(subary.copy()))
    
        return result
    
    def maxProductLeftAndRightScan(self, nums: List[int]) -> int:
        leftMax, rightMax = float('-inf'), float('-inf')
        product = 1
        for n in nums:
            product *= n
            leftMax = max(leftMax, product)
            if n==0:
                product = 1
        
        product = 1
        for n in nums[::-1]:
            product *= n
            rightMax = max(rightMax, product)
            if n==0:
                product = 1
        
        return max(leftMax, rightMax)
    
    def maxProductSingleScan(self, nums: List[int]) -> int:
        result = max(nums)
        curMin, curMax = 1, 1
        for n in nums:
            tmp = curMin
            curMin = min(curMin*n, curMax*n, n)
            curMax = max(tmp*n, curMax*n, n)
            result = max(result, curMax)
        return result
            
        

        

#nums = [0, 0, 2, 4, 0, 3, 3, 0, 0, -2, 4, 0, 0]
nums = [-3, -1, -1]
solver = Solution()

print(solver.maxProductLeftAndRightScan(nums))

