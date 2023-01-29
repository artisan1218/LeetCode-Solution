#!/usr/bin/env python
# coding: utf-8

# In[54]:


class Solution:
    def mySqrtIncrementOne(self, x: int) -> int:
        if x == 0:
            return 0
        else:
            ans = 1
            while (ans * ans) <= x:
                ans+=1
            return ans-1
        
    def mySqrtBinarySearch(self, x: int) -> int:
        if x == 0:
            return 0
        else:
            limit = 1
            while (limit * limit) <= x:
                limit*=2
       
        for ans in range(limit//2, limit+1):
            if (ans * ans) == x:
                return ans
            elif (ans * ans) > x:
                return ans-1
            
    def mySqrtNewton(self, x: int) -> int:
        ans = x
        while ans*ans > x:
            ans = (ans + x//ans) // 2
        return ans
        
if __name__ == "__main__":
    solver = Solution()
    x = 9
    print(solver.mySqrtNewton(x))


# In[ ]:




