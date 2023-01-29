#!/usr/bin/env python
# coding: utf-8

# In[5]:


from itertools import zip_longest

class Solution:
    def compareVersionZip(self, version1: str, version2: str) -> int:
        split1 = version1.split('.')
        split2 = version2.split('.')
        
        for d1, d2 in zip(split1, split2):
            if int(d1) < int(d2):
                return -1
            elif int(d1) > int(d2):
                return 1
            
        if len(split1) > len(split2):
            for i in range(len(split2), len(split1)):
                if int(split1[i]) > 0:
                    return 1
        else:
            for i in range(len(split1), len(split2)):
                if int(split2[i]) > 0:
                    return -1
        return 0
    
    def compareVersionZipLongest(self, version1: str, version2: str) -> int:
        split1 = version1.split('.')
        split2 = version2.split('.')
        
        for d1, d2 in zip_longest(split1, split2):
            d1 = int(d1) if d1!=None else 0
            d2 = int(d2) if d2!=None else 0
            if d1 < d2:
                return -1
            elif d1 > d2:
                return 1
        return 0
    
version1 = "1.01"
version2 = "1.001.9"
solver = Solution()
print(solver.compareVersionZipLongest(version1, version2))


# In[ ]:




