# N-Queens II problem
* The n-queens puzzle is the problem of placing `n` queens on an `n x n` chessboard such that no two queens attack each other.
* Given an integer `n`, return the number of distinct solutions to the n-queens puzzle.


### Approach 1: Return length of result list, Skipped
The naive solution is simply to return the length of result list that contians all the placement of queens, but since we are not interested in the exact position of queens, we can remove some of the variable that keeps track of the position of the queens to save time and space.

### Approach 2: Backtracking, backtracking()
The structure of this approach is similar to approach 1 except for the fact that there are no more variables used to store the exact placement of queens. We can simply replace it using another integer and return the integer only.

Time complexity is O(n!) where n is the number of queens.
![image](https://user-images.githubusercontent.com/25105806/126397376-d2ba91db-1b07-444b-8924-7e727930de7d.png)

