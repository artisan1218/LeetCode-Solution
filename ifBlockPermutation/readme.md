# Generate all permutations of if blocks
* Given a number of if blocks `n`, generate all ways of printing the `n` if blocks
* For example when `n=3`
```
if{
}
if{
}
if{
}
----------------------------
if{
}
if{
  if{
  }
}
----------------------------
if{
  if{
  }
}
if{
}
----------------------------
if{
  if{
    if{
    }
  }
}
```

### Approach 1: DFS
The idea is to first generate all permutations of the number of if blocks.\
For example when `n=3`, there are in total of 4 ways of printing: `[1,1,1], [1,2], [2,1], [3]`. Each number in the list represents the level of nested if blocks. 1 means 1 level nested if block, which is just a if block, 2 means 2 level nested if block, which is a if block inside another if block, etc. This is done by using recursion with backtracking, we will first generate a list from 1 to `n` representing all possible level of nested blocks we can take from, then find all permutations of these numbers that sum up to `n` because this is the valid permutation.\
The second step is then printing out the blocks given the level of a if block, this is done by using recursion, where we recursively print opening if block `if{` and then call recursion to print another opening if block `if{` until we've printed all blocks.


```python3
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
```

