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

