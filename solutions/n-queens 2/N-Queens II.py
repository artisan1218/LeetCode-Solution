#!/usr/bin/env python
# coding: utf-8

# In[10]:


from typing import List

class Solution:
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
        

if __name__ == "__main__":
    solver = Solution()
    n = 4
    result = solver.totalNQueens(n)
    print(result)


# In[ ]:




