#!/usr/bin/env python
# coding: utf-8

# In[8]:


from typing import List

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []
        
        counter = dict()
        for i in range(0, len(s)-9):
            seq = s[i:i+10]
            if seq not in counter:
                counter[seq] = 1
            else:
                counter[seq] += 1
        return [seq for seq in counter if counter[seq]>1]
        
        
if __name__ == '__main__':
    solver = Solution()
    s = "AAAAAAAAAAA"
    print(solver.findRepeatedDnaSequences(s))


# In[ ]:




