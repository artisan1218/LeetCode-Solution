#!/usr/bin/env python
# coding: utf-8

# In[58]:


from typing import List
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        self.backtrack(s, result, [], 0)
        return ['.'.join(address) for address in result]
        
    def backtrack(self, s, result, current, start):
        if start<=len(s) and len(current)<=4: # pruning
            if len(current)==4 and sum([len(digit) for digit in current])==len(s):
                result.append(current.copy())
            else:
                for i in range(1, 4): # only get up to next 3 letters
                    digit = s[start:start+i]
                    if len(digit)==1 or (len(digit)>1 and digit[0]!='0' and int(digit)<=255):
                        current.append(digit)
                        self.backtrack(s, result, current, start+i)
                        current.pop()
        
if __name__ == '__main__':
    solver = Solution()
    s = "0000"
    results = solver.restoreIpAddresses(s)
    print(results)


# In[ ]:




