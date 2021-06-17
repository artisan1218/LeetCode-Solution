#!/usr/bin/env python
# coding: utf-8

# In[36]:


from typing import List

class Solution:
    def isValidSudokuThreePass(self, board: List[List[str]]) -> bool:
        # check if each row contains the digits 1-9 without repetition.
        for row in board:
            checkSet = set()
            for digit in row:
                if digit.isdigit():
                    if digit not in checkSet:
                        checkSet.add(digit)
                    else:
                        return False
        
        # check if each column contains the digits 1-9 without repetition.
        for column in zip(*board):
            checkSet = set()
            for digit in column:
                if digit.isdigit():
                    if digit not in checkSet:
                        checkSet.add(digit)
                    else:
                        return False
                
        # check if each of the nine 3 x 3 sub-boxes of the grid contains the digits 1-9 without repetition.
        num_box_row = 3 # there are 3 sub-boxes in each row of the entire board
        num_box_column = 3 # there are 3 sub-boxes in each column of the entire board
        for sub_box_row in range(num_box_row):
            for sub_box_col in range(num_box_column):
                checkSet = set()
                for row in range(3*sub_box_row, 3*sub_box_row+3):
                    for col in range(3*sub_box_col, 3*sub_box_col+3):
                        digit = board[row][col]
                        if digit.isdigit():
                            if digit not in checkSet:
                                checkSet.add(digit)
                            else:
                                return False
        return True
    
    def isValidSudokuOnePass(self, board: List[List[str]]) -> bool:
        
        # digit in each row is encoded as variable 'row'
        # digit in each column is encoded as varibale 'col'
        # digit in each sub-box is encoded as variable 'box'
        # dividing i and j by 3 will give the index of sub-boxes so that we can differentiate them
        # this way we distinguish digits from different row, columns and sub-boxes
        # we only need one pass over the entire board to solve this
        
        seen = set()
        for i in range(len(board)):
            for j in range(len(board[i])):
                digit = board[i][j]
                if char!='.':
                    row = digit + ' in row ' + str(i)
                    col = digit + ' in col ' + str(j)
                    box = digit + ' in box ' + str(int(i/3)) + '-' + str(int(j/3))
                    if row not in seen and col not in seen and box not in seen:
                        seen.add(row)
                        seen.add(col)
                        seen.add(box)
                    else:
                        return False
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
    print(solver.isValidSudokuOnePass(board))


# In[ ]:




