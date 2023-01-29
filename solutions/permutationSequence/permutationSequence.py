#!/usr/bin/env python
# coding: utf-8

# In[57]:


import math

class Solution:
    
    def getPermutationOutsideIn(self, n: int, k: int) -> str:
        result = ''
        digits = [i+1 for i in range(n)]
        # we will iterate through each digit of the permutation
        
        '''
        n = 4, we have {1, 2, 3, 4}
        If you were to list out all the permutations you have

        1 + (permutations of 2, 3, 4)
        2 + (permutations of 1, 3, 4)
        3 + (permutations of 1, 2, 4)
        4 + (permutations of 1, 2, 3)
        
        we can first get the outer digit of the permutation, then work outside in.
        e.g. 
        solving 1 + (permutations of 2, 3, 4) 
        solving 2 + (permutations of 3, 4) 
        solving 4 + (permutations of 3)
        solving 3
        
        '''
        for _ in range(n):
            # nums is the number of permutations of n that start with same number
            # to put another word, there is nums group of permutation, each group starts with same digit
            nums = math.factorial(len(digits)-1)
            # since the permutation is in order, we can find the nth number in a group according to k
            nth = (k-1)//nums
            result+=str(digits[nth])
            # we've added this digit, so remove it from the digit list
            digits.remove(digits[nth])
            # update k in order to get the correct nth number in n-1 permutation
            k = k%nums
        
        return result
    
    def getPermutationPackage(self, n: int, k: int) -> str:
        from itertools import permutations
        return ''.join(list(permutations([str(i+1) for i in range(n)]))[k-1])
         

if __name__ == '__main__':
    solver = Solution()
    n = 4
    k = 7
    print(solver.getPermutationPackage(n, k))

