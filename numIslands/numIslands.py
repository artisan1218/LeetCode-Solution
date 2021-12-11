# %%
from typing import List

class Solution:
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

if __name__ == '__main__':
    grid = [["1","0","1","1","0","1","1"]]

    solver = Solution()
    print(solver.numIslands(grid))

# %%



