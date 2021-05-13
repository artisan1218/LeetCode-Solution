# Add Two Numebrs problem
* You are given two non-empty linked lists representing two non-negative integers. 
* The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
* You may assume the two numbers do not contain any leading zero, except the number 0 itself.

All three approaches have time complexity of O(m+n)
### Approach 1: addTwoNumbersMathSlow()
Iterate through both linked list at the same time, add the corresponding digits at same position, keep the carryover digit and compute the next digit. This pretty straight-forward. But several egde cases to consider: 
* two numbers are not the same length
* carryover digit is the last digit, which means one more digit it needed to generate the answer

### Approach 2: addTwoNumbersMathQuick()
Similar to approach 1 but improve the logic, remove uncessary blocks and make it faster. 

![image](https://user-images.githubusercontent.com/25105806/118186463-9ea4f380-b3f2-11eb-9dff-25e5bbcd933f.png)


### Approach 3: addTwoNumbersConversion()
Can also read the two linked list first, convert them to java BigInteger, do the math and convert the BigInteger back to linked list. This approach requires the use of BigInteger because the number might be too large for regular int in java. Thus the running time is slower than approach 2.

![image](https://user-images.githubusercontent.com/25105806/118186596-c4ca9380-b3f2-11eb-9290-0937f89b8116.png)
