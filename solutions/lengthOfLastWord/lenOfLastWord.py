#!/usr/bin/env python
# coding: utf-8

# In[41]:


class Solution:
    def lengthOfLastWordStripAndSplit(self, s: str) -> int:
        return len(s.strip().split(' ')[-1])
    
    def lengthOfLastWordLoop(self, s: str) -> int:
        result = 0
        for char in reversed(s):
            if char!=' ':
                result+=1
            elif result>0:
                return result
        return result
    
if __name__ == '__main__':
    solver = Solution()
    s = "a "
    print(solver.lengthOfLastWordLoop(s))


# In[ ]:




