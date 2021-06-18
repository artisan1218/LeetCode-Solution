# Valid Sudoku problem
Determine if a `9 x 9` Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
1. Each row must contain the digits `1-9` without repetition.
2. Each column must contain the digits `1-9` without repetition.
3. Each of the nine `3 x 3` sub-boxes of the grid must contain the digits `1-9` without repetition.

Note:
* A Sudoku board (partially filled) could be valid but is not necessarily solvable.
* Only the filled cells need to be validated according to the mentioned rules.

  ![image](https://user-images.githubusercontent.com/25105806/122307617-888dc580-cebf-11eb-8e27-20141b63e55f.png)


### Approach 1: Naive, Check All Three Rules in Three Pass, isValidSudokuThreePass()
This approach is very straightforward. Simply use three code blocks to check all three rules respectively.\
Time complexity is therefore O(3 \* n^2), which is O(n^2) where n is the side length of the board:
![image](https://user-images.githubusercontent.com/25105806/122307731-c68ae980-cebf-11eb-9690-4c0383cccb5e.png)

<br />

### Approach 2: One Pass, isValidSudokuOnePass()
The idea is to encode row number, column number and sub-box number along with the digit in each slot so that we can distinguish digit from different rows, columns or sub-boxes and therefore can check all three rules in one pass over the entire board.
* digit in each row is encoded as variable 'row'
* digit in each column is encoded as varibale 'col'
* digit in each sub-box is encoded as variable 'box'
* dividing i and j by 3 will give the index of sub-boxes so that we can differentiate them
     
     
Time complexity is therefore O(n^2):

![image](https://user-images.githubusercontent.com/25105806/122308035-66487780-cec0-11eb-81d4-d3114c4029e7.png)

