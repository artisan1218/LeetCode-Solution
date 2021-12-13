# Valid Sudoku problem
Determine if a `9 x 9` Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
1. Each row must contain the digits `1-9` without repetition.
2. Each column must contain the digits `1-9` without repetition.
3. Each of the nine `3 x 3` sub-boxes of the grid must contain the digits `1-9` without repetition.

Note:
* A Sudoku board (partially filled) could be valid but is not necessarily solvable.
* Only the filled cells need to be validated according to the mentioned rules.

  ![image](https://user-images.githubusercontent.com/25105806/122307617-888dc580-cebf-11eb-8e27-20141b63e55f.png)

Leetcode link: https://leetcode.com/problems/valid-sudoku/

<br/>

### Approach 1: Naive, Check All Three Rules in Three Pass, isValidSudokuThreePass()
This approach is very straightforward. Simply use three code blocks to check all three rules respectively.\

```python
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
```

Time complexity is therefore O(3 \* n^2), which is O(n^2) where n is the side length of the board:
![image](https://user-images.githubusercontent.com/25105806/122307731-c68ae980-cebf-11eb-9690-4c0383cccb5e.png)

<br />

### Approach 2: One Pass, isValidSudokuOnePass()
The idea is to encode row number, column number and sub-box number along with the digit in each slot so that we can distinguish digit from different rows, columns or sub-boxes and therefore can check all three rules in one pass over the entire board.
* digit in each row is encoded as variable 'row'
* digit in each column is encoded as varibale 'col'
* digit in each sub-box is encoded as variable 'box'
* dividing i and j by 3 will give the index of sub-boxes so that we can differentiate them
     
```python
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
```
     
Time complexity is therefore O(n^2):\
![image](https://user-images.githubusercontent.com/25105806/122308035-66487780-cec0-11eb-81d4-d3114c4029e7.png)

