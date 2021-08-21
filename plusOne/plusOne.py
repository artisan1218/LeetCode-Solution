#!/usr/bin/env python
# coding: utf-8

# In[10]:


from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        carryOn = True
        i = len(digits)-1
        while carryOn:
            if i<0:
                # 999 -> 1000
                digits.insert(0, 1)
                break
            else:
                digits[i] += 1
                if digits[i] == 10:
                    # 459 -> 460
                    digits[i] = 0
                    i -= 1
                else:
                    # 123 -> 124
                    carryOn = False
                
        return digits
            
        
if __name__ == "__main__":
    solver = Solution()
    digits = [9, 9, 9]
    print(solver.plusOne(digits))


# In[ ]:




