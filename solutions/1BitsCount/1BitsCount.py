#!/usr/bin/env python
# coding: utf-8

# In[2]:


class Solution:
    def hammingWeightLoopAllDigits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            ans += (n >> i) & 1
        
        return ans
    
    def hammingWeightLoopOnes(self, n: int) -> int:
        ans = 0
        while n:
            n = n & (n-1)
            ans+=1
        
        return ans
        
        
solver = Solution()
n = 0b00000000000000000000000000001011
print(solver.hammingWeightLoopOnes(n))


# In[ ]:




