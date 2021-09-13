#!/usr/bin/env python
# coding: utf-8

# In[2]:


from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rowNum = len(board)
        colNum = len(board[0])
        
        for row in range(rowNum):
            for col in range(colNum):
                if board[row][col] == word[0]:
                    curLen = 0
                    charIdx = 0
                    visited = set()
                    result = self.backtrack(board, word, curLen, rowNum, colNum, row, col, charIdx, visited)
                    if result:
                        return True
        
        return False
    
    def backtrack(self, board, word, curLen, rowNum, colNum, row, col, charIdx, visited):
        if curLen==len(word):
            return True
        else:
            if col<colNum and row<rowNum and col>=0 and row>=0                and (board[row][col]==word[charIdx])                and (row, col) not in visited:
                visited.add((row, col))
                r1 = self.backtrack(board, word, curLen+1, rowNum, colNum, row, col-1, charIdx+1, visited) # go left
                r2 = self.backtrack(board, word, curLen+1, rowNum, colNum, row, col+1, charIdx+1, visited) # go right
                r3 = self.backtrack(board, word, curLen+1, rowNum, colNum, row-1, col, charIdx+1, visited) # go up
                r4 = self.backtrack(board, word, curLen+1, rowNum, colNum, row+1, col, charIdx+1, visited) # go down
                # removed the visited row,col after trying all directions so that it will not affect the
                # next matching
                visited.remove((row, col))
                return r1 or r2 or r3 or r4
            else:                    
                return False

        
if __name__ == '__main__':
    board = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
    word = "ABCESEEEFS"
    solver = Solution()
    print(solver.exist(board, word))

