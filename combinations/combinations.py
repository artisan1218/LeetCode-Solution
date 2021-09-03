#!/usr/bin/env python
# coding: utf-8

# In[58]:


from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result =[]
        current = []
        start = 1
        self.backtrack(result, current, n, k, start)
        return result
        
    def backtrack(self, result, current, n, k, start):
        if len(current) == k:
            result.append(current.copy())
        else:
            for i in range(start, n+1):
                # only proceed when we have enough numbers
                if len(current) + n - i + 1 >= k:
                    current.append(i)
                    self.backtrack(result, current, n, k, i+1)
                    current.pop()
        
        
if __name__ == '__main__':
    solver = Solution()
    n = 4
    k = 2
    result = solver.combine(n, k)
    print(result)


# In[ ]:




