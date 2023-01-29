#!/usr/bin/env python
# coding: utf-8

# In[15]:


class Solution:
    def isNumber(self, s: str) -> bool:
        
        state = 0
        acceptState = {3, 6, 7, 8, 10}
        for char in s:
            if state==0:
                if char=='+' or char=='-':
                    state = 1
                elif char.isnumeric():
                    state = 7
                elif char=='.':
                    state = 9
                else:
                    return False
            elif state==1:
                if char=='.':
                    state = 2
                elif char.isnumeric():
                    state = 7
                else:
                    return False
            elif state==2:
                if char.isnumeric():
                    state = 3
                else:
                    return False
            elif state==3:
                if char=='e' or char=='E':
                    state = 4
                elif char.isnumeric():
                    state = 3
                else:
                    return False
            elif state==4:
                if char=='+' or char=='-':
                    state = 5
                elif char.isnumeric():
                    state = 10
                else:
                    return False
            elif state==5:
                if char.isnumeric():
                    state = 6
                else:
                    return False
            elif state==6:
                if char.isnumeric():
                    state = 6
                else:
                    return False
            elif state==7:
                if char.isnumeric():
                    state = 7
                elif char=='.':
                    state = 8
                elif char=='e' or char=='E':
                    state = 4
                else:
                    return False
            elif state==8:
                if char.isnumeric():
                    state = 3
                elif char=='e' or char=='E':
                    state = 4
                else:
                    return False
            elif state==9:
                if char.isnumeric():
                    state = 8
                else:
                    return False
            elif state==10:
                if char.isnumeric():
                    state = 10
                else:
                    return False
                
        return state in acceptState

    
if __name__ == "__main__":
    solver = Solution()
    s = ".0e7"
    print(solver.isNumber(s))

