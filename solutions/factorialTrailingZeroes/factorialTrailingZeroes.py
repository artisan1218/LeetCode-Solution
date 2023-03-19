#!/usr/bin/env python
# coding: utf-8

# In[41]:


class Solution:
    def trailingZeroesBruteForce(self, n: int) -> int:
        if n==0:
            return 0
        
        fact = 1
        while n>0:
            fact = fact * n
            n-=1
        
        fact_str = str(fact)
        zeros = 0
        i = len(fact_str) - 1
        while fact_str[i] == '0':
            zeros+=1
            i-=1
        return zeros
    
    def trailingZeroesMath(self, n: int) -> int:
        result = 0
        fiveMultiple = 5
        while n >= fiveMultiple:
            result += n//fiveMultiple
            fiveMultiple *= 5
        return result
    
solver = Solution()
n = 200
print(solver.trailingZeroesMath(n))


# In[ ]:




