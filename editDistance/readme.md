# Edit Distance problem
* Given two strings word1 and word2, return the minimum number of operations required to convert `word1` to `word2`.
* You have the following three operations permitted on a word:
  1. Insert a characte.
  2. Delete a character.
  3. Replace a character
 
### Approach 1: Dynamic Programming, minDistance()
The idea is very straightforward and comes from the definition of 'dividing': that is, how many `divisors` are contained in `dividend`. We simply subtract divisor from dividend once a time until `dividend` is smaller than `divisor`, which means `dividend` does not contain `divisor` anymore. \
For example: we divide 5000 by 14:
* We can subtract 14 from 5000 for 357 times: 14\*357=4998 and 5000-4998=2 and 2<14. quotient = 357


The main downside of this approach is:
1. When the dividend(2^31-1) is large and divisor is small(1), the running time is slow because we simply subtract 1 from 2^31-1 2^31-1 times.
2. Hard to handle overflow issue

Time complexity is therefore O(n/m) where n is the value of `dividend` and m is the value of `divisor`.\
Note that this approach definitely works, but this will lead to ETL on leetcode.com

<br />

### Approach 2, Bit-wise Manipulation, divide()

Credits to: https://www.youtube.com/watch?v=We3YDTzNXEk

The dynamic programming will build 2-d matrix from `word1` and `word2`. Each slot represents the number of edits needed to convert from word1 to word2:\
For example, the top-left corner has a value of 0, which means converting `''` to `''` requires 0 edit, while 2 at the first row means converting `'hor'` to `''` requires 3 edits.

<img src="https://user-images.githubusercontent.com/25105806/130541915-9dc25d56-92f3-4846-babe-9f2aad4d04d6.jpg" width="50%" height="50%">

We can initialize first row and first column easily. Starting from position `[1][1]`, there are two cases to consider:
1. If the character `c1` corresponding to row and character `c2` corresponding to column is the same, then it requires no more extra edit to convert, we can simply set the value as `matrix[row-1][col-1]`. For example converting from `'ho'` to `'ro'` requires the same amount of edits as to converting from `'h'` to `'r'` because they both share `'o'`
2. If the character `c1` and `c2` are not the same, then the value should be the minimum edit distances among all three neighbors plus one. 1 here means we need one more edit than whatever the smallest edit distance is. 

Keep filling out the matrix and return the `dp[-1[-1]`

Time complexity is O(mn) where `m` is the size of `word1` and `n` is the size of `word2`:\
![image](https://user-images.githubusercontent.com/25105806/130542771-16f019d7-4d00-4944-a1cc-73531e3fc30c.png)

