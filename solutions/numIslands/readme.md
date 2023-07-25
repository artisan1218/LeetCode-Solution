# Number of Islands problem
Given an `m x n` 2D binary grid grid which represents a map of `'1'`s (land) and `'0'`s (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 
```
Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
```

Leetcode link: https://leetcode.com/problems/number-of-islands/

<br />

### Approach 1: DFS, numIslands()
Explore all cells in the matrix line by line and for each land(`1`) we meet, enter a DFS to explore all its connected neighbor and change all visited cells to `0` so that we don't visit them again. Then simply increase the counter by 1 and check for the next cell.

```python
def numIslands(self, grid: List[List[str]]) -> int:
    def helper(grid, r, c):
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
            return
        else:
            if grid[r][c] == '1':
                grid[r][c] = '0' # we have visited this cell, mark it as visited
                helper(grid, r+1, c)
                helper(grid, r-1, c)
                helper(grid, r, c+1)
                helper(grid, r, c-1)
            return

    count = 0
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == '1':
                count+=1
                helper(grid, r, c)
                print(grid)
    return count
```

Time complexity is O(n+m) where `n` is the total number of cells in the matrix `grid` and `m` is the total number of lands:\
![image](https://user-images.githubusercontent.com/25105806/145692741-da367c37-9b49-425b-a9ae-615fff1996ad.png)

