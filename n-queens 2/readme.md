# N-Queens problem
* The n-queens puzzle is the problem of placing `n` queens on an `n x n` chessboard such that no two queens attack each other.
* Given an integer `n`, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.
* Each solution contains a distinct board configuration of the n-queens' placement, where `'Q'` and `'.'` both indicate a queen and an empty space, respectively.
* Two queens will attack each other if one of the queen is on the same row, same column or same diagonal with the other queen
  ![image](https://user-images.githubusercontent.com/25105806/126275030-771e1037-fb49-4f17-90de-8dc768ef9f3a.png)



### Approach 1: Backtracking, backtracking()

The problem is very similar to Sudoku question solved [here](https://github.com/artisan1218/LeetCode-Solution/tree/main/sudokuSolver). We will first setup some functions to check for valid placement of a queen and to update board. `board` is used to represent the board in a 2d list, each element of the 2d list is also a list, we will append if this spot is valid(`True` or `False`) given each new placement of queens so that we can keep track of the validness if backtracking a queen placement.\
The idea is to use recursion to try each possible spot to place the queen. If a place is valid, then we enter the recursive function again to check for the next valid position until we've placed all queens on the board. Note that we will actually check row by row because of a simply insight: each row must have 1 and at least 1 queen, so we will know this configuration is valid if there is a valid spot in the last row of board. 

Reference: https://leetcode.com/problems/n-queens/discuss/243428/Python-solution and https://www.youtube.com/watch?v=xouin83ebxE

Time complexity is O(n!) where n is the number of queens.
![image](https://user-images.githubusercontent.com/25105806/126276495-766e476e-1977-4bad-bdd4-43d6187aa854.png)

