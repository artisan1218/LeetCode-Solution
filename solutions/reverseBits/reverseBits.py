#!/usr/bin/env python
# coding: utf-8

# In[45]:


class Solution:
    def reverseBitsLoop(self, n: int) -> int:
        res = 0
        for i in range(32):
            # get the last digit, since & 1 will only work on the unit digit of the shifted number
            bit = (n >> i) & 1
            # bit << (31 - i) to build a number of length 31-i, pad with 0
            # then take the or with res to append it to the end of res
            res = res | (bit << (31 - i))

        return res
    
    def reverseBitsDivideAndConquer(self, n: int) -> int:
        
        n = (n >> 16) | (n << 16);
        n = ((n & 0b11111111000000001111111100000000) >> 8) | ((n & 0b00000000111111110000000011111111) << 8);
        n = ((n & 0b11110000111100001111000011110000) >> 4) | ((n & 0b00001111000011110000111100001111) << 4);
        n = ((n & 0b11001100110011001100110011001100) >> 2) | ((n & 0b00110011001100110011001100110011) << 2);
        n = ((n & 0b10101010101010101010101010101010) >> 1) | ((n & 0b01010101010101010101010101010101) << 1);
        return n
    
    
solver = Solution()
n = 0b00000010100101000001111010011100
print(solver.reverseBitsDivideAndConquer(n))

