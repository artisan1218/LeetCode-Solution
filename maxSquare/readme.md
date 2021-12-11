# Maximal Square problem
* Given an `m x n` binary matrix filled with `0's` and `1's`, find the largest square containing only `1's` and return its area.

Leetcode link: https://leetcode.com/problems/maximal-square/

<br/>

### Approach 1: Dynamic Programming, maximalSquare()
Credits to: https://www.youtube.com/watch?v=_Lf1looyJMU&list=PLPF7kEFdTM01pt_t39BC5nWdju4eskICf&index=3

The idea is to build a dp matrix, first row and first column is simply copy of the first row and first column of `matrix`. Starting at position (1,1), each cell is dependent on the minimal value of the three neighbors around it, namely, `min(dp[row-1][col], dp[row][col-1], dp[row-1][col-1]) + 1`. Then simply return the square of the maximal value.

```python
def maximalSquare(self, matrix: List[List[str]]) -> int:
    maxSide = 0

    dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    # init first row and first column
    for col in range(len(matrix[0])):
        if matrix[0][col]=='1':
            dp[0][col]=1
            maxSide = 1
    for row in range(len(matrix)):
        if matrix[row][0]=='1':
            dp[row][0]=1
            maxSide = 1

    # dp starts here. Each new cell in dp in dependent on the minimal value of the three neightbors around it.
    for row in range(1, len(matrix)):
        for col in range(1, len(matrix[row])):
            if matrix[row][col]=='1':
                dp[row][col] = min(dp[row-1][col], dp[row][col-1], dp[row-1][col-1]) + 1
            else:
                dp[row][col] = 0
            maxSide = max(maxSide, dp[row][col])

    return maxSide**2
```

Time complexity is O(mn) where m and n is the height and width of the `matrix`:\
![image](https://user-images.githubusercontent.com/25105806/133669677-3ab85f80-52e8-436b-b538-d5c9c013e60a.png)
