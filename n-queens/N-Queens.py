#!/usr/bin/env python
# coding: utf-8

# In[2]:


from typing import List

class Solution:
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

if __name__ == "__main__":
    solver = Solution()
    n = 4
    result = solver.solveNQueens(n)
    print(result)


# In[ ]:




