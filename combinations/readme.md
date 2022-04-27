# Combinations problem
* Given two integers `n` and `k`, return all possible combinations of `k` numbers out of the range `[1, n]`.

Leetcode link: https://leetcode.com/problems/combinations/

<br />

### Approach 1: Backtracking, combine()
Classical backtracking problem. Use backtrack to explore all possible combinations and us pruning to skip the invalid answer. For example if `n=4` and current list is `[1,4]`, we can skip this because we do no have enough values to add to the curren list

```python3
def combine(self, n: int, k: int) -> List[List[int]]:
    result =[]
    current = []
    start = 1
    self.backtrack(result, current, n, k, start)
    return result

def backtrack(self, result, current, n, k, start):
    if len(current) == k:
        result.append(current.copy())
    else:
        for i in range(start, n+1):
            # only proceed when we have enough numbers
            if len(current) + n - i + 1 >= k:
                current.append(i)
                self.backtrack(result, current, n, k, i+1)
                current.pop()
```

Actual running time:\
<img width="654" alt="image" src="https://user-images.githubusercontent.com/25105806/132046287-693c7d9a-8a14-4ce8-8cc5-95920773e74e.png">



