# Add Binary problem
* Given two binary strings `a` and `b`, return their sum as a binary string.

### Approach 1: Math, addBinary()
Since `a` and `b` are given as strings and they might have different length, we first pad the shorter string with 0 to make it as long as the longer string. Then simply use python `zip()` function to add the digits vertically.

Time complexity is O(n):

![957d46d1ff4ad47efe8745dc7461a70](https://user-images.githubusercontent.com/25105806/130334479-9e85c23a-1d9e-475d-a27e-293a97936d61.png)
