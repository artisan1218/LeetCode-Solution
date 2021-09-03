# Combinations problem
* Given two integers `n` and `k`, return all possible combinations of `k` numbers out of the range `[1, n]`.


### Approach 1: Backtracking, combine()
Classical backtracking problem. Use backtrack to explore all possible combinations and us pruning to skip the invalid answer. For example if `n=4` and current list is `[1,4]`, we can skip this because we do no have enough values to add to the curren list\

Actual running time:\
<img width="654" alt="image" src="https://user-images.githubusercontent.com/25105806/132046287-693c7d9a-8a14-4ce8-8cc5-95920773e74e.png">



