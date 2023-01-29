# Minimum Path Sum problem
* Given a `m x n` `grid` filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.
* Note: You can only move either down or right at any point in time.

Leetcode link: https://leetcode.com/problems/minimum-path-sum/

<br />

### Approach 1: Brute Force, Skipped
Since we can compute all unique paths using dfs recursion, we can sum up the values along the path and take the minimum sum as the result. But this approach is not time efficient. Skipped.

<br />

### Approach 2: Dynamic Programming, minPathSum()
This solution is similar to the DP solution in [uniquePaths II](https://github.com/artisan1218/LeetCode-Solution/tree/main/uniquePaths%20II), we first work out the sum of path for the first row and first column, then from (1, 1), sum up the cell value with the minimum sum of cell value above it or left of it, this way we can make sure that at each cell, the value is the minimum sum of path value so far. The final result is therefore at `grid[-1][-1]`


```python3
def minPathSum(self, grid: List[List[int]]) -> int:
    numRow = len(grid)
    numCol = len(grid[0])

    # sum up the first row
    for col in range(1, numCol):
        grid[0][col] += grid[0][col-1]

    # sum up first column
    for row in range(1, numRow):
        grid[row][0] += grid[row-1][0]

    # dp part
    for row in range(1, numRow):
        for col in range(1, numCol):
            grid[row][col] += min(grid[row-1][col], grid[row][col-1])

    return grid[-1][-1]
```


Running time complexity is O(n):\
![572526aec123063f4e91c22c405b1fd](https://user-images.githubusercontent.com/25105806/130027535-03e13f53-ed21-4464-a3d0-9d3af22296a1.png)


    

