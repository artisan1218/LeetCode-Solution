# N-Queens problem
* The n-queens puzzle is the problem of placing `n` queens on an `n x n` chessboard such that no two queens attack each other.
* Given an integer `n`, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.
* Each solution contains a distinct board configuration of the n-queens' placement, where `'Q'` and `'.'` both indicate a queen and an empty space, respectively.
* Two queens will attack each other if one of the queen is on the same row, same column or same diagonal with the other queen
  ![image](https://user-images.githubusercontent.com/25105806/126275030-771e1037-fb49-4f17-90de-8dc768ef9f3a.png)


Leetcode link: https://leetcode.com/problems/n-queens/

<br />


### Approach 1: Backtracking, backtracking()

The problem is very similar to Sudoku question solved [here](https://github.com/artisan1218/LeetCode-Solution/tree/main/sudokuSolver). We will first setup some functions to check for valid placement of a queen and to update board. `board` is used to represent the board in a 2d list, each element of the 2d list is also a list, we will append if this spot is valid(`True` or `False`) given each new placement of queens so that we can keep track of the validness if backtracking a queen placement.\
The idea is to use recursion to try each possible spot to place the queen. If a place is valid, then we enter the recursive function again to check for the next valid position until we've placed all queens on the board. Note that we will actually check row by row because of a simply insight: each row must have 1 and at least 1 queen, so we will know this configuration is valid if there is a valid spot in the last row of board. 

Reference: https://leetcode.com/problems/n-queens/discuss/243428/Python-solution and https://www.youtube.com/watch?v=xouin83ebxE


```python3
def solveNQueens(self, n: int) -> List[List[str]]:
    result = []
    board = [[[True] for _ in range(n)] for _ in range(n)]
    current = [['.' for _ in range(n)] for _ in range(n)]
    self.backtracking(0, board, current, result, n)
    return result

def backtracking(self, row, board, current, result, n):
    if row == n:
        current_result = [''.join(rowList) for rowList in current]
        result.append(current_result)
        return

    for col in range(n):
        if self.isSafe2Place(col, row, board):
            # fill in the current board
            current[col][row] = 'Q'
            self.updateBoard(col, row, n, board, 'add')
            # check next row
            # if there is a solution, will append this board to result
            self.backtracking(row+1, board, current, result, n)
            # backtrack
            current[col][row] = '.'
            self.updateBoard(col, row, n, board, 'remove')

def isSafe2Place(self, x, y, board):
    return board[x][y][-1]

def updateBoard(self, x, y, n, board, mode):
    # new queen will be placed at x, y

    if mode=='add':
        # update the row
        for row in range(n):
            board[x][row].append(False)

        # update the column
        for col in range(n):
            board[col][y].append(False)

        # update diagonal, top left to bottom right
        i, j = x+1, y+1
        while i<n and j<n:
            board[i][j].append(False)
            i+=1
            j+=1    
        i, j = x-1, y-1
        while i>=0 and j>=0:
            board[i][j].append(False)
            i-=1
            j-=1

        # update diagonal, top right to bottom left
        i, j = x-1, y+1
        while i>=0 and j<n:
            board[i][j].append(False)
            i-=1
            j+=1
        i, j = x+1, y-1
        while i<n and j>=0:
            board[i][j].append(False)
            i+=1
            j-=1      
    else:
        # update the row
        for row in range(n):
            board[x][row].pop(-1)

        # update the column
        for col in range(n):
            board[col][y].pop(-1)

        # update diagonal, top left to bottom right
        i, j = x+1, y+1
        while i<n and j<n:
            board[i][j].pop(-1)
            i+=1
            j+=1    
        i, j = x-1, y-1
        while i>=0 and j>=0:
            board[i][j].pop(-1)
            i-=1
            j-=1

        # update diagonal, top right to bottom left
        i, j = x-1, y+1
        while i>=0 and j<n:
            board[i][j].pop(-1)
            i-=1
            j+=1
        i, j = x+1, y-1
        while i<n and j>=0:
            board[i][j].pop(-1)
            i+=1
            j-=1      
```

Time complexity is O(n!) where n is the number of queens.
![image](https://user-images.githubusercontent.com/25105806/126394168-788ab572-cc4d-4e09-ab15-db86bef07918.png)

