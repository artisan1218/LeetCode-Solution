# Unique Binary Search Trees problem
![image](https://user-images.githubusercontent.com/25105806/135387175-511bad80-5fa9-4eb8-b362-976c02a8a0ac.png)

Leetcode link: https://leetcode.com/problems/unique-binary-search-trees/

<br />

### Approach 1: Dynamic Programming, numTrees()
We can find the pattern as follows:

![image](https://user-images.githubusercontent.com/25105806/135387595-dc41348f-7a88-4c59-aa74-053627a32123.png)

`count[n]` means the number of unique BSTs with `n` nodes. Therefore, we can convert this problem to many subproblems.

The key lien of code to solve this is `cur += result[j] * result[i-j-1]`, where we iteratively calculate the number of sub-BSTs given different node as root. We will go through the case where each node between `[1,n]` is the root


```python3
def numTrees(self, n: int) -> int:
    result = [1]
    for i in range(1, n+1):
        cur = 0
        for j in range(i):
            # n=5: n=4*n=0 + n=3*n=1 + n=2*n=2 + n=1*n=3 + n=0*n=4
            cur += result[j] * result[i-j-1]
        result.append(cur)

    return result[-1]
```

Actual running time:

![image](https://user-images.githubusercontent.com/25105806/135387965-96f15b5f-86f6-4683-b8cb-a4fe114aca41.png)
