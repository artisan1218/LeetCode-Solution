# N-Queens II problem
* The n-queens puzzle is the problem of placing `n` queens on an `n x n` chessboard such that no two queens attack each other.
* Given an integer `n`, return the number of distinct solutions to the n-queens puzzle.

Leetcode link: https://leetcode.com/problems/n-queens-ii/

<br />

### Approach 1: Return length of result list, Skipped
The naive solution is simply to return the length of result list that contians all the placement of queens, but since we are not interested in the exact position of queens, we can remove some of the variable that keeps track of the position of the queens to save time and space.

<br />

### Approach 2: Backtracking, backtracking()
The structure of this approach is similar to approach 1 except for the fact that there are no more variables used to store the exact placement of queens. We can simply replace it using another integer and return the integer only.


```python3
def totalNQueens(self, n: int) -> int:
    board = [[[True] for _ in range(n)] for _ in range(n)]
    return self.backtracking(0, board)

def backtracking(self, row, board):
    count = 0
    if row == len(board):
        return 1

    for col in range(len(board)):
        if self.isSafe2Place(col, row, board):
            self.updateBoard(col, row, board, True)
            # check next row
            # if there is a solution, will append this board to result
            count += self.backtracking(row+1, board)
            # backtrack
            self.updateBoard(col, row, board, False)

    return count

def isSafe2Place(self, x, y, board):
    return board[x][y][-1]

def updater(self, x, y, board, isAdd):
    if isAdd:
        board[x][y].append(False)
    else:
        board[x][y].pop(-1)

def updateBoard(self, x, y, board, isAdd):
    # new queen will be placed at x, y

    # update the row
    for row in range(len(board)):
        self.updater(x, row, board, isAdd)

    # update the column
    for col in range(len(board)):
        self.updater(col, y, board, isAdd)

    # update diagonal, top left to bottom right
    i, j = x+1, y+1
    while i<len(board) and j<len(board):
        self.updater(i, j, board, isAdd)
        i+=1
        j+=1    
    i, j = x-1, y-1
    while i>=0 and j>=0:
        self.updater(i, j, board, isAdd)
        i-=1
        j-=1

    # update diagonal, top right to bottom left
    i, j = x-1, y+1
    while i>=0 and j<len(board):
        self.updater(i, j, board, isAdd)
        i-=1
        j+=1
    i, j = x+1, y-1
    while i<len(board) and j>=0:
        self.updater(i, j, board, isAdd)
        i+=1
        j-=1      
```

Time complexity is O(n!) where n is the number of queens.
![image](https://user-images.githubusercontent.com/25105806/126397376-d2ba91db-1b07-444b-8924-7e727930de7d.png)

