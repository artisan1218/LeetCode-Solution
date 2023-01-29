#!/usr/bin/env python
# coding: utf-8

# In[58]:


import math

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator % denominator == 0:
            return str(numerator//denominator)
        
        res = '' if ((numerator>0) == (denominator>0)) else '-' # sign
        num, den = map(abs, (numerator, denominator))
        res += str(num//den) # int part
        res += '.'
        
        remainder = num % den
        index_map = dict()
        """
        for example: 611 ÷ 4950
        
         611    ÷ 4950 = 0...611
         611*10 ÷ 4950 = 1...1160
        1160*10 ÷ 4950 = 2...1700
        1700*10 ÷ 4950 = 3...2150
        2150*10 ÷ 4950 = 4...1700 (we get 1700 again, so first the occurrence is the start of 
        repeating pattern and this occurrence is the end of repeating pattern)
        """
        # the first time we see repeated remainder is where repeating pattern ends
        # so the loop while generate a decimal number repeating only once
        while remainder not in index_map:
            index_map[remainder] = len(res)
            res += str(remainder*10 // den) # next digit
            remainder = remainder*10 % den
            if remainder==0:
                return res
            
        # index_map[remainder] is where repeating starts    
        return res[:index_map[remainder]] + '(' + res[index_map[remainder]:] + ')'

numerator = 611
denominator = 4950
solver = Solution()
print(solver.fractionToDecimal(numerator, denominator))

