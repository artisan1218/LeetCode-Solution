# ZigZag Conversion problem
* The string `"PAYPALISHIRING"` is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
  ```
  P   A   H   N
  A P L S I I G
  Y   I   R
  ```
  And then read line by line: `"PAHNAPLSIIGYIR"`\
  Write the code that will take a string and make this conversion given a number of rows:
  `string convert(string s, int numRows);`

### Approach 1: Traverse in ZigZag Order, convert()
There is a pattern existed in the zigzag printout any string: the index of the line-by-line order string will skip two parts of the zigzag shape alternately, I call them bottom part and top part.
* bottom part will decrease by two for each row starting from the number `2 * numRows - 2`, which is the number of skipped chars for the first row: `skippedBottom -= 2`
* top part will increase by two for each row starting from 0: `skippedTop += 2`
All we need to do is to control the switching of these two number and append the characters at corresponding index of `i += skippedBottom` or `i += skippedTop`.

     <img src="https://user-images.githubusercontent.com/25105806/118089937-c1e18b80-b37d-11eb-804a-e22539362e41.png" width="80%" height="80%">
The whole process is like: charAt(i), skip bottom, charAt(i+bottom), skip top, charAt(i+top), starts at new row, charAt(i), skip bottom, ...
Even though I used nested loop in the implemention, the time complexity is still O(n) because the outer loop will go through each row and the inner loop will will not go through all indices of the chars but only chars at that specific row, so the total number of indices visited is strictly equal to the total number of characters, thus O(n).\
We can see that the running time is indeed quite fast
![image](https://user-images.githubusercontent.com/25105806/118090743-c490b080-b37e-11eb-9d1a-9ad69a8cb5ea.png)
