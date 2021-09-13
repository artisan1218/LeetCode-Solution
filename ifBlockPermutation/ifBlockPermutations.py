#!/usr/bin/env python
# coding: utf-8

# In[11]:


def generatePermutations(nums, target):
    result = []
    helper(nums, target, result, [])
    return result

def helper(nums, target, result, current):
    currentSum = sum(current)
    # current sum is equal to target sum, we have found a permutation
    if currentSum==target:
        result.append(current.copy())
    elif currentSum < target: # current sum if smaller than target sum, we need to add more
        # 1 1 -> 1 1 1
        for num in nums:
            current.append(num)
            helper(nums, target, result, current)
            current.pop()
                
def printBlocks(level, indentation):
    # level is the remaining if block we should print
    if level!=0:
        print(''.ljust(indentation) + 'if{') # print indentation and opening if block
        printBlocks(level-1, indentation+2) # print nested if blocks
        print(''.ljust(indentation) + '}') # print indentation and closing if block

if __name__ == "__main__":
    n = 3
    nums = list(range(1, n+1))
    permutations = generatePermutations(nums, n)

    for permutation in permutations:
        for num in permutation:
            printBlocks(num, 0) # default indentation is 0
        print('----------------------------')


# In[ ]:




