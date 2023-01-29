#!/usr/bin/env python
# coding: utf-8

# In[2]:


from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        else:
            res = [[1], [1, 1]]
            for lvl_idx in range(2, numRows):
                level = [1]
                for j in range(1, lvl_idx):
                    level.append(res[-1][j-1] + res[-1][j])
                level.append(1)
                res.append(level)
            return res

if __name__ == '__main__':
    solver = Solution()
    numRows = 10
    result = solver.generate(numRows)
    print(result)


# In[ ]:




