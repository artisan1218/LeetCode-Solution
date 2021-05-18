# String to Integer (atoi) problem
* Implement the `myAtoi(string s)` function, which converts a string to a 32-bit signed integer (similar to C/C++'s `atoi` function).
* The algorithm for myAtoi(string s) is as follows:
  1. Read in and ignore any leading whitespace.
  2. Check if the next character (if not already at the end of the string) is `'-'` or `'+'`. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
  3. Read in next the characters until the next non-digit charcter or the end of the input is reached. The rest of the string is ignored.
  4. Convert these digits into an integer (i.e. `"123" -> 123`, `"0032" -> 32`). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
  5. If the integer is out of the 32-bit signed integer range `[-2^31, 2^31 - 1]`, then clamp the integer so that it remains in the range. Specifically, integers less than `-2^31` should be clamped to `-2^31`, and integers greater than `2^31 - 1` should be clamped to `2^31 - 1`.
  6. Return the integer as the final result.

### Approach 1: String Traversal, myAtoiNaive()
This approach is the native solution, which is easily to come up with, simply go through the string `s`, check each char and make corresponding actions.\
Time complexity is simply O(n) because we only visit each of the chars in the string `s` once.\
![image](https://user-images.githubusercontent.com/25105806/118205932-63b4b700-b416-11eb-9dd8-32adf6f0119d.png)

### Approach 2: DFA(Deterministic Finite Automaton), myAtoiDFA()
Credits to: https://leetcode.com/problems/string-to-integer-atoi/discuss/798380/Fast-and-simpler-DFA-approach-(Python-3)

This approach utilizes the DFA to implement the logic behind this question. Turns out we can use three states to represent the logic of this question:
1. Space state, which can go to Space, Digit, or Sign state. If the current char is not `' '`, not `'+'` or `'-'` and not a digit, should simply return 0(reject state)
2. Sign state, which can only to go Digit state. If current char is not digit, simply return 0(reject state)
3. Digit state, which can only go to Digit state. If current char is not a digit, return the current value(reject state)

We will still go through each char of the string `s`, then decide which state to go depends on the value of `s` and the current state.\
The DFA is shown below:\
<img src="https://user-images.githubusercontent.com/25105806/118206316-16851500-b417-11eb-97ae-82cfea4b4f8a.png" height="70%" width="70%">

Time complexity is also O(n) because we only visit each of the chars in the string `s` once.\
![image](https://user-images.githubusercontent.com/25105806/118206818-251ffc00-b418-11eb-97b4-741c4fa944d3.png)


