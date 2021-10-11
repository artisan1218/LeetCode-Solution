# Maximal Rectangle problem
* Given a rows `x` cols binary matrix filled with `0's` and `1's`, find the largest rectangle containing only `1's` and return its area.

### Approach 1: Dynamic Programming, maximalRectangle()
This solution is build upon the [maximalRectangleInHistogram](https://github.com/artisan1218/LeetCode-Solution/tree/main/largestRecInHist). We will convert the max rectangle problem to max rectangle in histogram by iterating the `matrix` row by row and summing up the values in each column to get `heights`, then simply use the solution for max rectangle in histogram to solve the problem iteratively. 

Time complexity is O(mn) where m and n is the width and height of the `matrix`:
![image](https://user-images.githubusercontent.com/25105806/133670735-aa7b95cb-543c-46a1-ad05-da232bd8ddb4.png)

