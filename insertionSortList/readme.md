# Interleaving String problem
![image](https://user-images.githubusercontent.com/25105806/135661455-24d6246a-7602-45a8-a5a9-ed0f681e236f.png)


Leetcode link: https://leetcode.com/problems/interleaving-string/

<br />

### Approach 1: Backtrack, isInterleaveBacktrack()
The idea is to explore every possible combinations of the cut position at `s1` and `s2`. This is a exhaustive solution so the running time is relatively slow. We can use memorization (`@lru_cache()`) to speed up.

```python3
@lru_cache()
def isInterleaveBacktrack(self, s1: str, s2: str, s3: str) -> bool:
    if len(s1)==0 and len(s2)==0 and len(s3)==0:
        return True
    elif len(s1)+len(s2)!=len(s3):
        return False
    else:
        res1 = False
        for i in range(1, len(s1)+1):
            if s1[:i]==s3[:i]:
                res1 = self.isInterleave(s1[i:], s2, s3[i:])
                if res1==True:
                    return True
                else:
                    break
            else:
                break

        res2 = False
        for i in range(1, len(s2)+1):
            if s2[:i]==s3[:i]:
                res2 = self.isInterleave(s1, s2[i:], s3[i:])
                if res2==True:
                    return True
                else:
                    break
            else:
                break

        return res1 or res2
```

Time complexity is O(2^(m+n)) where m is the length of `s1` and n is the length of `s2`
![image](https://user-images.githubusercontent.com/25105806/135661878-a7c86ee2-84cf-4d73-975a-2e0d0d0d1efa.png)


<br />

### Approach 2: Dynamic Programming with Recursion, isInterleaveDP1()
Credits to https://www.youtube.com/watch?v=3Rw3p9LrgvE

This is somehow similar to approach 1, but this time we simply use two ints `i` and `j` to represent the cut position, and use a dict `dp` to cache the seen cases so that we do not calculate again.

```python3
def isInterleaveDP1(self, s1: str, s2: str, s3: str) -> bool:
    dp = {}
    def dfs(i, j):
        if i==len(s1) and j==len(s2):
            return True
        if (i, j) in dp:
            return dp[(i, j)]

        if i<len(s1) and s1[i] == s3[i+j] and dfs(i+1, j):
            return True
        if j<len(s2) and s2[j] == s3[i+j] and dfs(i, j+1):
            return True

        dp[(i, j)] = False
        return False

    if len(s1)+len(s2)!=len(s3):
        return False
    else:
        return dfs(0, 0)
```

Time complexity is O(m\*n):\
![image](https://user-images.githubusercontent.com/25105806/135662332-bb11ccdf-ef69-4a5d-bcf1-b00530a52e91.png)


<br />

### Approach 3: Dynamic Programming with Iteration, isInterleaveDP2()
Credits to https://www.youtube.com/watch?v=ih2OZ9-M3OM

Instead of using recursion, we can also construct a 2d dp array to solve this question. Similar to other dp questions, we use `s1` and `s2` as row and column, each position `(i, j)` at the 2d array `dp` represent whether we can form the first `(i+j)` substring using `s1[:i] and s2[:j]`. Then simply return `dp[-1][-1]`

The rules for updating dp is as follows:
1.  If `s1[i]` matches `s3[i+j]`, then we need to check whether `s2[j-1]` is valid. If both of them are `True`, we can update `dp[i][j]` to `True`
2.  If `s2[j]` matches `s3[i+j]`, then we need to check whether `s1[i-1]` is valid. If both of them are `True`, we can update `dp[i][j]` to `True`


```python3
def isInterleaveDP2(self, s1: str, s2: str, s3: str) -> bool:
    if len(s1)+len(s2)!=len(s3):
        return False
    else:
        dp = [[False for _ in range(len(s1)+1)] for _ in range((len(s2)+1))]  
        dp[0][0] = True

        # initialize first row
        for i in range(len(s1)):
            if s1[i] == s3[i] and dp[0][i]==True:
                dp[0][i+1] = True

        # initialize first column
        for i in range(len(s2)):
            if s2[i] == s3[i] and dp[i][0]==True:
                dp[i+1][0] = True

        for row in range(1, len(s2)+1):
            for col in range(1, len(s1)+1):
                if s1[col-1] == s3[row+col-1] and dp[row][col-1] == True:
                    dp[row][col] = True

                if s2[row-1] == s3[row+col-1] and dp[row-1][col] == True:
                    dp[row][col] = True

        return dp[-1][-1]
```

Time complexity is O(m\*n):\
![image](https://user-images.githubusercontent.com/25105806/135662988-e64fc8b1-1a0f-40ef-b220-8e8e27195c7c.png)

