#!/usr/bin/env python
# coding: utf-8

# In[42]:


class Solution:
    def numTrees(self, n: int) -> int:
        
        result = [1]
        for i in range(1, n+1):
            cur = 0
            for j in range(i):
                # n=5: n=4*n=0 + n=3*n=1 + n=2*n=2 + n=1*n=3 + n=0*n=4
                cur += result[j] * result[i-j-1]
            result.append(cur)
        
        return result[-1]
        
if __name__ == '__main__':
    solver = Solution()
    n = 5
    print(solver.numTrees(n))


# In[ ]:




