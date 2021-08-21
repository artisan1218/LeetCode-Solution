#!/usr/bin/env python
# coding: utf-8

# In[31]:


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        result = ''
        maxLen = max(len(a), len(b))
        # padding
        a = a.rjust(maxLen, '0')
        b = b.rjust(maxLen, '0')

        carry = 0
        for a_digit, b_digit in zip(reversed(a), reversed(b)):
            digit = int(a_digit) + int(b_digit) + carry
            # 1 + 1
            if digit==2:
                digit = 0
                carry = 1
            # 1 + 1 + 1, 1 is carry on digit
            elif digit==3:
                digit = 1
                carry = 1
            # 1 + 0 or 0 + 0
            else:
                carry = 0
            result = str(digit) + result
            
        if carry == 1:
            result = '1' + result
        return result

if __name__ == "__main__":
    solver = Solution()
    a = "1111"
    b = "1111"
    print(solver.addBinary(a, b))


# In[ ]:




