#!/usr/bin/env python
# coding: utf-8

# In[21]:


class Solution:
    
    # exhaust all possible paths
    def climbStairsRecursion(self, n: int) -> int:
        return self.helper(0, n)
        
    def helperRecursion(self, cur, n):
        result = 0
        if cur == n:
            result = 1
        else:
            if cur+1 <= n:
                result += self.helperRecursion(cur+1, n)
            
            if cur+2 <= n:
                result += self.helperRecursion(cur+2, n)
        return result
        
    # similar to fibonacci series, use recursion with memorization to calculate 
    def climbStairsMath(self, n: int) -> int:
        cache = {}
        return self.helperMath(n, cache)
        
    def helperMath(self, n, cache):
        if n<=3:
            result = n
        else:
            if n-1 not in cache.keys():
                a = self.helperMath(n-1, cache)
                cache[n-1] = a
                
            if n-2 not in cache.keys():
                b = self.helperMath(n-2, cache)
                cache[n-2] = b
            
            result = cache[n-1] + cache[n-2]
            
        return result
    
    # use iteration to calculate, store all seen values in a list
    def climbStairsIteration1(self, n: int) -> int:
        if n<=3:
            return n
        else:
            result = [1,2,3]
            for _ in range(n-3):
                result.append(result[-1] + result[-2])
        return result[-1]
        
    # use iteration to calculate, only keeping two variables
    def climbStairsIteration2(self, n: int) -> int:
        if n<=3:
            return n
        else:
            a, b = 2, 3
            for _ in range(n-3):
                c = a + b
                a = b
                b = c
        return b
    
    
if __name__ == "__main__":
    solver = Solution()
    n = 8
    print(solver.climbStairsIteration2(n))


# In[14]:


34-21


# In[ ]:




