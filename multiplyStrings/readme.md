# Multiply Strings problem
* Given two non-negative integers `num1` and `num2` represented as strings, return the product of `num1` and `num2`, also represented as a string.
* Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.


### Approach 1: Math, multiply()
This approach is really the very definition of multiplication, we can divide a multiplication into this:

`123 * 456` can be splited into `100*400 + 100*50 + 100*6 + 20*400 + 20*50 + 20*6 + 3*400 + 3*50 + 3*6`. That is, each digit with its magnitude in `num1` multiply each digit with magnitude in `num2` and we sum them up to get the result\
We simply use two for-loop to do this, outer loop is to iterate through each digit of the longer number, inner loop is to iterate through each digit of the shorter number, then we multiply them together

Time complexity is O(m\*n) where m is the length of `num1` and n is the length of `num2`:
![image](https://user-images.githubusercontent.com/25105806/123171061-26d5da00-d430-11eb-8965-29e608bd82f3.png)

    

