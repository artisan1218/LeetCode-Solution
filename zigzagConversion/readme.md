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
  
Leetcode link: https://leetcode.com/problems/zigzag-conversion/

<br/>

### Approach 1: Traverse in ZigZag Order, convert()
There is a pattern existed in the zigzag printout any string: the index of the line-by-line order string will skip two parts of the zigzag shape alternately, I call them bottom part and top part.
* bottom part will decrease by two for each row starting from the number `2 * numRows - 2`, which is the number of skipped chars for the first row: `skippedBottom -= 2`
* top part will increase by two for each row starting from 0: `skippedTop += 2`

All we need to do is to control the switching of these two number and append the characters at corresponding index of `i += skippedBottom` or `i += skippedTop`.

<img src="https://user-images.githubusercontent.com/25105806/118091542-cc048980-b37f-11eb-9be4-1cff27607429.png" width="100%" height="100%">

* Note: For the right-most figure, `bottom = 4` and `top = 6`, then `i = 3`, `i = 3 + 4 = 7`, `i = 3 + 4 + 6 = 13` for chars at pos 3, 7, 13, respectively.

The whole process is like: charAt(i), skip bottom, charAt(i=i+bottom), skip top, charAt(i=i+top), starts at new row, charAt(i), skip bottom, ...
Even though I used nested loop in the implemention, the time complexity is still O(n) because the outer loop will go through each row and the inner loop will will not go through all indices of the chars but only chars at that specific row, so the total number of indices visited is strictly equal to the total number of characters, thus O(n).

```java
public static String convert(String s, int numRows) {
	if (numRows == 1) {
	    return s;
	} else {
	    StringBuilder result = new StringBuilder("");
	    int row = 0;
	    // skippedNum is the number of chars that we need to skip in order to get the
	    // string in line-by-line order if the string is printed in zigzag order
	    int skippedNum = 2 * numRows - 2;
	    int i = 0;
	    // skippedBottom is the number of chars that we need to skip at the bottom part
	    // of the zigzag shaped string (v shape), while skippedTop is the number of
	    // chars that we need to skip at the top part of the zigzag shaped string (^
	    // shape).
	    int skippedBottom = skippedNum;
	    int skippedTop = 0;
	    boolean switch2Bottom = true;

	    while (row < numRows) {
		i = row; // i starts at the row index, which is the first char in that row
		switch2Bottom = true;
		if (row == 0 || row == numRows - 1) {
		    while (i < s.length()) {
			result.append(s.charAt(i));
			i += skippedNum;
		    }
		} else {
		    skippedBottom -= 2;
		    skippedTop += 2;
		    while (i < s.length()) {
			result.append(s.charAt(i));
			// switching between these two different skipped number we can control the pace
			// of i, which controls chars to be appended
			if (switch2Bottom) {
			    i += skippedBottom;
			    switch2Bottom = false;
			} else {
			    i += skippedTop;
			    switch2Bottom = true;
			}
		    }
		}
		row++;
	    }
	    return result.toString();
	}
    }

```

We can see that the running time is indeed quite fast:\
![image](https://user-images.githubusercontent.com/25105806/118090743-c490b080-b37e-11eb-9d1a-9ad69a8cb5ea.png)
