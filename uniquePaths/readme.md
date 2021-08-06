# Unique Paths problem
* A robot is located at the top-left corner of a `m x n` grid (marked `'Start'` in the diagram below).
* The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked `'Finish'` in the diagram below).
* How many possible unique paths are there?
  ![image](https://user-images.githubusercontent.com/25105806/128464614-2974f9f3-3bc7-4bca-9c0e-5442547cda48.png)


### Approach 1: DFS, uniquePathsDFS()
The idea is that we can explore different paths in a tree structure using DFS algorithm. That is, for any given point in the grid, we can first go to right, then go down and repeat the process recursively until we hit the finish point.
This DFS approach is simple but it is slow and lead to TLE :(


### Approach 2: Math, uniquePathsMathNaive()
If we denote a grid using a tuple of `m` and `n`, for example `(5,3)`, then there is a pattern for us to utilize: the number of paths in grid `(5,3) = (4,3) + (5,2)`, and we can solve this equation recursively until one of the `m` and `n` is 1, which is the base case because `(1, n)` or `(m, 1)` is 1. The structure of this solution is also simple but since we do not store/cache any calculated value, which means we have to calculate each grid separately using recursion, this is also very slow and lead to TLE. But the good news is we can optimize it.


### Approach 3: Math 2, uniquePathsMathOptimized()
Instead of calculating each possible grid separately, we can use a python dict to store the seen grid tuple and use it rightaway if needed. This may use more space but saves lots of time. 

Actual running time:
![c0cf1bd1abd857e43d1f8a133130740](https://user-images.githubusercontent.com/25105806/128465383-d395f041-b7ed-403a-89d4-8afe618cdf10.png)


