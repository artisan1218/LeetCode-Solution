# Word Search problem
* Given an `m x n` grid of characters board and a string word, return `true` if word exists in the grid.
* The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Leetcode link: https://leetcode.com/problems/word-search/

<br />

### Approach 1: Backtracking, exist()
First loop through each cell in the board to find all possible starting point for the matching: if the first char is matched, then this is a potential start of the matching, which means we should call backtrack() to check.\
In backtrack(), the exit condition is when the length of the found word `curLen` is equal to the length of target `word`. We will check all four directions to go if the index of row or column is within the range of the `board` matrix and the characters are matched and `(row, col)` is not in `visited`, which means this cell has not been visited.\
Importantly, after trying all four directions, we should remove the current cell from the visited set because this will affect the next checking, this is where backtracking happens.

```python3
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
        if col<colNum and row<rowNum and col>=0 and row>=0 and (board[row][col]==word[charIdx]) and (row, col) not in visited:
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
```

Actual running time:\
![image](https://user-images.githubusercontent.com/25105806/132603068-68e9ceb3-f33a-4d56-a595-c3e790024574.png)

