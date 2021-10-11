#!/usr/bin/env python
# coding: utf-8

# In[5]:


from typing import List

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        pre = matrix[0].copy()
        dp = matrix[0].copy()
        for r in range(1, rows):
            for c in range(cols):
                left = pre[max(0, c-1)] # max(0, c-1) is to bound the range when c=0
                mid = pre[c]
                right = pre[min(cols-1, c+1)] # min(cols-1, c+1) is to bound the range when c=cols
                dp[c] = matrix[r][c] + min(left, mid, right)
            pre = dp.copy()
            
        return min(dp)

if __name__ == '__main__':
    solver = Solution()
    matrix = [[2,1,3],[6,5,4],[7,8,9]]
    result = solver.minFallingPathSum(matrix)
    print(result)


# In[ ]:




