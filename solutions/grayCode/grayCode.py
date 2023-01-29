#!/usr/bin/env python
# coding: utf-8

# In[29]:


from typing import List

class Solution:
    def grayCodeBacktrack(self, n: int) -> List[int]:
       
        def backtrack(n, curBin, result, used):
            result.append(curBin)
            used.add(curBin)

            if len(result) < 2**n:
                curBin = result[-1]
                for i in range(len(curBin)):
                    # change one digit
                    curBin = curBin[:i] + '1' + curBin[i+1:] if curBin[i]=='0' else curBin[:i] + '0' + curBin[i+1:]
                    if curBin not in used:
                        # we've found a valid change
                        break
                    else:
                        # change it back since this is not a valid option
                        curBin = curBin[:i] + '1' + curBin[i+1:] if curBin[i]=='0' else curBin[:i] + '0' + curBin[i+1:]

                backtrack(n, curBin, result, used)
        
        start = ''.join(['0' for _ in range(n)])
        binaryResult = []
        backtrack(n, start, binaryResult, set())
        
        return [int(binary, 2) for binary in binaryResult]
        
    def grayCodeBit(self, n: int) -> List[int]:
        result = []
        for i in range(1<<n):
            result.append(i^(i>>1))
        return result
    
if __name__ == '__main__':
    solver = Solution()
    n = 3
    code = solver.grayCodeBit(n)
    print('result', code)


# In[ ]:




