# Maximal Square problem
* Given an `m x n` binary matrix filled with `0's` and `1's`, find the largest square containing only `1's` and return its area.


### Approach 1: Dynamic Programming, maximalSquare()
Credits to: https://www.youtube.com/watch?v=_Lf1looyJMU&list=PLPF7kEFdTM01pt_t39BC5nWdju4eskICf&index=3

The idea is to build a dp matrix, first row and first column is simply copy of the first row and first column of `matrix`. Starting at position (1,1), each cell is dependent on the minimal value of the three neighbors around it, namely, `min(dp[row-1][col], dp[row][col-1], dp[row-1][col-1]) + 1`. Then simply return the square of the maximal value.

Time complexity is O(mn) where m and n is the height and width of the `matrix`:
![image](https://user-images.githubusercontent.com/25105806/133669677-3ab85f80-52e8-436b-b538-d5c9c013e60a.png)
