#!/usr/bin/env python
# coding: utf-8

# In[6]:


from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        else:
            prevRow = [1, 1]
            for lvl_idx in range(2, rowIndex+1):
                curRow = [1]
                for j in range(1, lvl_idx):
                    curRow.append(prevRow[j-1] + prevRow[j])
                curRow.append(1)
                prevRow = curRow
            return curRow

if __name__ == '__main__':
    solver = Solution()
    rowIndex = 3
    result = solver.getRow(rowIndex)
    print(result)


# In[ ]:




