# Word Search problem
* Given an `m x n` grid of characters board and a string word, return `true` if word exists in the grid.
* The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

### Approach 1: Backtracking, exist()
First loop through each cell in the board to find all possible starting point for the matching: if the first char is matched, then this is a potential start of the matching, which means we should call backtrack() to check.\
In backtrack(), the exit condition is when the length of the found word `curLen` is equal to the length of target `word`. We will check all four directions to go if the index of row or column is within the range of the `board` matrix and the characters are matched and `(row, col)` is not in `visited`, which means this cell has not been visited.\
Importantly, after trying all four directions, we should remove the current cell from the visited set because this will affect the next checking, this is where backtracking happens.

Actual running time:\
![image](https://user-images.githubusercontent.com/25105806/132603068-68e9ceb3-f33a-4d56-a595-c3e790024574.png)

