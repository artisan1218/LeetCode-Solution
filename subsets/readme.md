# Sudoku Solver problem
Write a program to solve a Sudoku puzzle by filling the empty cells.\
A sudoku solution must satisfy all of the following rules:
1. Each of the digits `1-9` must occur exactly once in each row.
2. Each of the digits `1-9` must occur exactly once in each column.
3. Each of the digits `1-9` must occur exactly once in each of the 9 `3x3` sub-boxes of the grid.

The '.' character indicates empty cells.


  ![image](https://user-images.githubusercontent.com/25105806/122307617-888dc580-cebf-11eb-8e27-20141b63e55f.png)


### Approach 1: Backtracking, solveSudoku()
This approach takes idea from https://leetcode.com/problems/sudoku-solver/discuss/294215/Simple-concise-clear-Python-solution and this video expains the algorithm very well: https://www.youtube.com/watch?v=eqUwSA0xI-s

We basically find an empty slot denoted by `'.'` row by row  and start guessing numbers from 1 to 9 that can be filled in at this spot. If the number is valid(meet all three requirements mentioned above), then we will update the `board` with this number and use recursion to find the next empty slot. If, at some point, there are no numbers can validate the sudoku, we should quit the current recursion stack and backtrack the digit filled previously by changing the slot back to `'.'`\
I use three check lists `row_check`, `col_check` and `box_check` to make the checking faster using only constant time by storing unqiue numbers in each row, each columns and each sub-boxes in sets and update them along the way.

Time complexity is O(n + 9^m) where `n` is the number of all digits in the `board` and `m` is the number of digits that we need to fill in. O(n) is to build the initial check lists and O(9^m) is to exhaust all possible combinations recursively.\
Actual running time:

![image](https://user-images.githubusercontent.com/25105806/122506456-404fcf80-cfb3-11eb-95a7-531a2512d9ae.png)




