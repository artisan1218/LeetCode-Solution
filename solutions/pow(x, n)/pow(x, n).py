#!/usr/bin/env python
# coding: utf-8

# In[60]:


class Solution:
    def myPow(self, x: float, n: int) -> float:
       
        absN = abs(n)
        result = 1
        while absN>0:
            if absN%2==1:
                result *= x
            x *= x
            absN = absN//2
        return result if n>=0 else 1/result
    
if __name__ == "__main__":
    x = 2
    n = 3
    solver = Solution()
    print(solver.myPow(x, n))


# In[ ]:




