#!/usr/bin/env python
# coding: utf-8

# In[29]:


from typing import List

class Solution:

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # initialize three list of sets that records the filled numbers for all rows, columns and boxes
        row_check = [set() for _ in range(9)]
        col_check = [set() for _ in range(9)]
        box_check = [set() for _ in range(9)]

        # fill in the check lists by scanning the initial board
        for i in range(9):
            for j in range(9):
                digit = board[i][j]
                if digit!='.':
                    row_check[i].add(digit)
                    col_check[j].add(digit)
                    # box in box_check is indexed from 0 to 9
                    # (i//3)*3 + (j//3) is to convert i and j to index 0 to 9
                    box_check[(i//3)*3 + (j//3)].add(digit)
        
        self.backtrack(board, 0, 0, row_check, col_check, box_check)
        
    def backtrack(self, board: List[List[str]], row: int, col: int, row_check, col_check, box_check) -> bool:
        # find the empty slot where we can fill in a digit
        while board[row][col]!='.':
            col+=1
            if col==9:
                col = 0
                row += 1
            if row==9:
                # this means we've checked all rows and columns and there is no problem, we can return valid
                return True

        # find an empty slot, begin filling in
        # simply try from 1 to 9, because each one of them might be possible
        for filling in range(1, 10):
            # use check list to check if the current filling is valid
            isValidFilling = self.isValidFilling(board, row, col, str(filling), row_check, col_check, box_check)
            if isValidFilling:
                # this filling does not violate the rules, we can change it in place now
                board[row][col] = str(filling)
                # this is a valid filling for now, we should update the check list
                self.updateCheckList(row, col, row_check, col_check, box_check, str(filling), 'add')
                
                # we should keep checking the rest slots starting from this slot
                isValidSubFillings = self.backtrack(board, row, col, row_check, col_check, box_check)
                if isValidSubFillings:
                    return True
                else:
                    # this is where backtracking happens
                    # if the filling lead to invalid sudoku, remove it from row_check, col_check and box_check
                    self.updateCheckList(row, col, row_check, col_check, box_check, str(filling), 'delete')
                    # change the filling back to empty slot
                    board[row][col] = '.'
                    # check the next filling
                    
        # we've check all numbers and none of them fit, which means the previous filling is invalid
        return False
    
    def updateCheckList(self, row, col, row_check, col_check, box_check, filling, mode):
        if mode=='add':
            row_check[row].add(filling)
            col_check[col].add(filling)
            box_check[(row//3)*3 + (col//3)].add(filling)
        elif mode=='delete':
            row_check[row].discard(filling)
            col_check[col].discard(filling)
            box_check[(row//3)*3 + (col//3)].discard(filling)
                
    def isValidFilling(self, board, row, col, filling, row_check, col_check, box_check):
        if filling in row_check[row]: return False
        if filling in col_check[col]: return False
        if filling in box_check[(row//3)*3 + (col//3)]: return False
        return True
        
        
if __name__ == "__main__":
    solver = Solution()
    board = [["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
    solver.solveSudoku(board)
    for row in board:
        print(row)
        


# In[ ]:




