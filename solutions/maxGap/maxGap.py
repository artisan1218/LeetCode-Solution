#!/usr/bin/env python
# coding: utf-8

# In[1]:


from typing import List
import math

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        minNum = min(nums)
        maxNum = max(nums)
        n = len(nums)
        
        if minNum == maxNum:
            return 0  # all nums are the same
        else:
            bucketSize = math.ceil((maxNum-minNum) / (n-1))
            # since we only need to store the min and max value in each bucket, 
            # we can simply use two bucket lists to represent the min and max at each bucket
            minBuckets = [float('inf')] * n
            maxBuckets = [float('-inf')] * n
            for num in nums:
                idx = (num - minNum) // bucketSize # find out which bucket num belongs to
                minBuckets[idx] = min(minBuckets[idx], num)
                maxBuckets[idx] = max(maxBuckets[idx], num)
                
            # maxGap can be initialized to bucketSize because maxGap is always greater 
            # or equal to bucketSize, why? Because we have n buckets but we evenly 
            # distribute the all possible numbers in nums(maxNum-minNum) into n-1 ranges
            # which means, at least one bucket must be empty according to pigeon hole's principle
            # So the max gap must be between two buckets and the empty bucket must be next to
            # one of the two buckets.
            maxGap = bucketSize 
            prevMax = maxBuckets[0]
            for i in range(1, n):
                if minBuckets[i] == float('inf'):
                    continue # skip the empty bucket
                else:
                    # subtract max value in previous bucket from current min value 
                    maxGap = max(maxGap, minBuckets[i] - prevMax)
                    prevMax = maxBuckets[i]
            return maxGap
    
    
solver = Solution()
nums = [3,6,9,1,15]
# nums = [100,3,2,1]
print(solver.maximumGap(nums))


# In[ ]:




