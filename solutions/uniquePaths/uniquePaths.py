#!/usr/bin/env python
# coding: utf-8

# In[73]:


class Solution:
    def uniquePathsDFS(self, m: int, n: int) -> int:
        result = self.dfs(m, n, 0, 0)
        return result
    
    def dfs(self, m, n, row, col):
        result = 0
        # find the finish point
        if row == m-1 and col == n-1:
            return 1
        else:
            # go to right
            if col<n-1:
                result+=self.dfs(m, n, row, col+1)
            # go down
            if row<m-1:
                result+=self.dfs(m, n, row+1, col)
        return result
    
    def uniquePathsMathNaive(self, m: int, n: int) -> int:
        result = 0
        if m==1 or n==1:
            return 1
        else:
            result += self.uniquePathsMathNaive(m-1, n) + self.uniquePathsMath(m, n-1)
            return result 
        
    def uniquePathsMathOptimized(self, m: int, n: int) -> int:
        return self.math(m, n, {})
        
    def math(self, m, n, cache):
        result = 0
        if m==1 or n==1:
            return 1
        else:
            if tuple((m-1, n)) in cache:
                num1 = cache[tuple((m-1, n))]
            else:
                num1 = self.math(m-1, n, cache)
                
            if tuple((m, n-1)) in cache:
                num2 = cache[tuple((m, n-1))]
            else:
                num2 = self.math(m, n-1, cache)
            
            # calculate the current result
            result += num1 + num2
            # cache the result so that we don't need to calculate again
            cache[tuple((m, n))] = result
            return result 
        
        
if __name__ == '__main__':
    m = 2
    n = 2
    solver = Solution()
    print(solver.uniquePathsMathOptimized(m, n))
        


# In[ ]:




