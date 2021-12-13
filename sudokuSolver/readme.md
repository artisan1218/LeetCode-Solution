# Sudoku Solver problem
Write a program to solve a Sudoku puzzle by filling the empty cells.\
A sudoku solution must satisfy all of the following rules:
1. Each of the digits `1-9` must occur exactly once in each row.
2. Each of the digits `1-9` must occur exactly once in each column.
3. Each of the digits `1-9` must occur exactly once in each of the 9 `3x3` sub-boxes of the grid.

The '.' character indicates empty cells.

![image](https://user-images.githubusercontent.com/25105806/122307617-888dc580-cebf-11eb-8e27-20141b63e55f.png)

Leetcode link: https://leetcode.com/problems/sudoku-solver/

<br/>

### Approach 1: Backtracking, solveSudoku()
This approach takes idea from https://leetcode.com/problems/sudoku-solver/discuss/294215/Simple-concise-clear-Python-solution and this video expains the algorithm very well: https://www.youtube.com/watch?v=eqUwSA0xI-s

We basically find an empty slot denoted by `'.'` row by row  and start guessing numbers from 1 to 9 that can be filled in at this spot. If the number is valid(meet all three requirements mentioned above), then we will update the `board` with this number and use recursion to find the next empty slot. If, at some point, there are no numbers can validate the sudoku, we should quit the current recursion stack and backtrack the digit filled previously by changing the slot back to `'.'`\
I use three check lists `row_check`, `col_check` and `box_check` to make the checking faster using only constant time by storing unqiue numbers in each row, each columns and each sub-boxes in sets and update them along the way.

```python
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
```

Time complexity is O(n + 9^m) where `n` is the number of all digits in the `board` and `m` is the number of digits that we need to fill in. O(n) is to build the initial check lists and O(9^m) is to exhaust all possible combinations recursively.\
Actual running time:\
![image](https://user-images.githubusercontent.com/25105806/122506456-404fcf80-cfb3-11eb-95a7-531a2512d9ae.png)




