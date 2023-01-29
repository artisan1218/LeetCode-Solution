# Distinct Subsequences problem
![image](https://user-images.githubusercontent.com/25105806/142576858-8a441fb6-7384-415c-85aa-44fc64292c69.png)

Leetcode link: https://leetcode.com/problems/distinct-subsequences/

### Approach 1: Backtrack, numDistinctBacktrack()
The idea is to use backtrack to exhaust all possible permutations of the sub-sequence. When the index `ti` reaches the end of target `t`, then we've found a solution and we should increment the counter by 1, otherwise just keeping iterating through all matches at the current position.

```python
def numDistinctBacktrack(self, s: str, t: str) -> int:
    def helper(s, t, si, ti):
        result = 0
        if ti==len(t):
            return 1
        else:
            for i in range(si, len(s)):
                if s[i] == t[ti]:
                    result += helper(s, t, i+1, ti+1)
            return result

    return helper(s, t, 0, 0)
```

This solution leads to TLE :(

<br />

### Approach 2, DFS, numDistinctDFS()
Credits to: https://www.youtube.com/watch?v=-RDzMJ33nx8&list=WL&index=1

The key idea is the two possible actions we can take when the two characters at `s` and `t` are the same. 
1.  We can either 'match' this character and go to check the next character at position `s[si+1]` and `t[ti+1]`
2.  Or we can skip this character as it is possible that there are more characters in the following substring that matches the character at current index `ti`. This way we should only check the next character in the `s` and keep the index `ti` unchanged.

We do this recursively in a DFS so at each matching index, we have two choices and this will cover all possible permutations. We need to use memorization technique to reduce the running time complexity.

```python
def numDistinctDFS(self, s: str, t: str) -> int:
    mem = dict()

    def dfs(si, ti):
        if (si, ti) in mem:
            return mem[(si, ti)]
        else:
            if ti==len(t):
                return 1
            elif si==len(s):
                return 0
            else:
                if s[si]==t[ti]:
                    mem[(si, ti)] = dfs(si+1, ti+1) + dfs(si+1, ti)
                else:
                    mem[(si, ti)] = dfs(si+1, ti)
                return mem[(si, ti)]

    return dfs(0, 0) # si and ti starts at 0
```

Time complexity is O(m\*n) where `m` and `n` are the length of `s` and `t`:\
![image](https://user-images.githubusercontent.com/25105806/142577861-468a40ee-8b2d-469d-b772-1779e9806cc3.png)


<br />

### Approach 3, Dynamic Programming, numDistinctDP()
The idea is similar to approach 2 but this time we use a 2d array `dp` to represent the memorization. The key idea is still the same: we have two choices at each matching index.


```python
def numDistinctDP(self, s: str, t: str) -> int:
    dp = [[0] * (len(s)+1) for _ in range(len(t) + 1)]

    for i in range(len(s)+1):
        dp[0][i] = 1

    for row in range(1, len(t)+1):
        for col in range(1, len(s)+1):
            if t[row-1]==s[col-1]:
                dp[row][col] = dp[row][col-1] + dp[row-1][col-1]
            else:
                dp[row][col] = dp[row][col-1]
    return dp[-1][-1]
```

Time complexity is O(m\*n):\
![image](https://user-images.githubusercontent.com/25105806/142578122-68717fef-1ef4-4711-939a-fd318c15b26a.png)

