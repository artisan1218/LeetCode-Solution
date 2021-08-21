# Unique Paths II problem
* A robot is located at the top-left corner of a `m x n` grid (marked 'Start' in the diagram below).
* The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
* Now consider if some obstacles are added to the grids. How many unique paths would there be?
* An obstacle and space is marked as `1` and `0` respectively in the grid.
  
  ![image](https://user-images.githubusercontent.com/25105806/129841820-e6eff4f4-4061-40cf-acfb-2d8cc8695141.png)   


### Approach 1: DFS, uniquePathsWithObstaclesDFS()
This approach is based on the similar approach in [uniquePath ](https://github.com/artisan1218/LeetCode-Solution/tree/main/uniquePaths). The only change is that when we choose the direction of next step, we first check for obstacle in the cell, if there is an obstacle, we simply skip this move.\
This DFS approach is simple but it is slow and lead to TLE :(

### Approach 2: Dynamic Programming, uniquePathsWithObstaclesDP()
Credits to https://leetcode.com/problems/unique-paths-ii/solution/

This solution is based on an observation that the numebr of paths that reache a certian cell is equal to the sum of number of paths reach the cell above it and left of it: 
`obstacleGrid[row][col] = obstacleGrid[row-1][col] + obstacleGrid[row][col-1]`

With this in mind, we can first work out the first column and first row because we can only go from above for the first column and we can only go from left for the first row. Then start at position `(1, 1)` of the matrix, simply scan over the entire matrix and sum up the number above it and left of it. 


Original matrix:\
<img src="https://user-images.githubusercontent.com/25105806/129842476-aa11dcba-f26b-4878-b733-481e01e351a5.png" width="30%" height="30%">

Matrix after we worked out first column and first row, noticed that 1 in the first column and first row simply means there is 1 path lead to the cell instead of an obstacle:\
<img src="https://user-images.githubusercontent.com/25105806/129842642-2caf2909-7a64-4fae-b70a-018b3828f8f4.png" width="30%" height="30%">

Summing up paths above and left of the (1, 1) cell, and keeping iterating through the entire matrix until we reach the end, which is the bottom right corner:\
<img src="https://user-images.githubusercontent.com/25105806/129842793-b5f838b3-3024-472e-86d0-c16e60243fa4.png" width="30%" height="30%">

Matrix after we've calculated all paths:\
<img src="https://user-images.githubusercontent.com/25105806/129842904-825d0432-97d0-4a23-9f0f-58d29d776040.png" width="30%" height="30%">


Time complexity is O(n) where `n` is the number of cells in the matrix:
![14f6ba783c6c62a7d27e2dcb74f2fc0](https://user-images.githubusercontent.com/25105806/129842408-48f6a52b-4c6f-4e16-bd92-e35800699a14.png)




