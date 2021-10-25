#!/usr/bin/env python
# coding: utf-8

# In[21]:


class Solution:
    def countBinarySubstringsGroup(self, s: str) -> int:
        groups = []
        prev = None
        for num in s:
            if prev==None or num!=prev:
                groups.append(1)
            else:
                groups[-1] += 1
            prev = num
        
        result = 0
        for i in range(len(groups)-1):
            result += min(groups[i], groups[i+1])
            
        return result
    
    def countBinarySubstringsOnePass(self, s: str) -> int:
        result = 0
        pre = 0
        cur = 1
        for i in range(1, len(s)):
            if s[i-1] != s[i]:
                # for the first time s[i-1] != s[i], pre is 0, so the result is 0
                # which means a group of 0 or 1 does not contribute to any valid result
                result += min(pre, cur)
                pre, cur = cur, 1
            else:
                cur += 1
    
        return result + min(pre, cur)
           
    
if __name__ == '__main__':
    solver = Solution()
    s = "00110011"
    print(solver.countBinarySubstringsOnePass(s))


# In[ ]:




