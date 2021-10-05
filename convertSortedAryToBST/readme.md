# Count and Say problem
The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
* `countAndSay(1) = "1"`
* `countAndSay(n)` is the way you would "say" the digit string from `countAndSay(n-1)`, which is then converted into a different digit string.

To determine how you "say" a digit string, split it into the minimal number of groups so that each group is a contiguous section all of the same character. Then for each group, say the number of characters, then say the character. To convert the saying into a digit string, replace the counts with a number and concatenate every saying.

For example, the saying and conversion for digit string `"3322251"`:
![image](https://user-images.githubusercontent.com/25105806/122621108-6b84fe00-d049-11eb-8d4d-2f3c63e7575a.png)

Given a positive integer `n`, return the nth term of the count-and-say sequence.


### Approach 1: Build the String From "1", countAndSay()
Simply follow the steps of building the count-and-say sequence, by first count the numbers of characters in each group and say the character, then appending to the end of `res`. Then go to the next string until we looped for `n` times.

```
n=1: 1, base case
n=2: 11, because there is one 1 in case n=1
n=3: 21, because there are two 1's in case n=2
n=4: 1211, because there are one 2 and one 1 in case n=3
n=5: 111221, because there are one 1, one 2, two 1's in case n=4
...
```

Time complexity is O(n\*m) where n is the positive integer `n` and `m` is the length of string built at each `n`:
![image](https://user-images.githubusercontent.com/25105806/122621400-4775ec80-d04a-11eb-8eeb-68c2745cc8ce.png)




