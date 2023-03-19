#!/usr/bin/env python
# coding: utf-8

# In[10]:


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        n = len(columnTitle)
        result = 0
        for c in columnTitle:
            result += (ord(c) - 64) * (26 ** (n-1))
            n -= 1
        return result

columnTitle = "ZY"
solver = Solution()
print(solver.titleToNumber(columnTitle))

