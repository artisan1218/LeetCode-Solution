# Count Binary Substrings problem
![image](https://user-images.githubusercontent.com/25105806/138642881-adc3fb4f-5bf7-4863-9acf-572749921f8a.png)

Leetcode link:https://leetcode.com/problems/count-binary-substrings/

<br />

### Approach 1: Group by Char, countBinarySubstringsGroup()
Reference: https://leetcode.com/problems/count-binary-substrings/solution/

The idea is to count the number of occurrences of each gruop of characters, then sum over the minimum value of each adjacent two groups to get the answer:

We can convert the string s into an array groups that represents the length of same-character contiguous blocks within the string. For example, if s = `"110001111000000"`, then `groups = [2, 3, 4, 6]`.

For every binary string of the form `'0' * k + '1' * k` or `'1' * k + '0' * k`, the middle of this string must occur between two groups.

Let's try to count the number of valid binary strings between `groups[i]` and `groups[i+1]`. If we have `groups[i] = 2`, `groups[i+1] = 3`, then it represents either `"00111"` or `"11000"`. We clearly can make `min(groups[i], groups[i+1])` valid binary strings within this string. Because the binary digits to the left or right of this string must change at the boundary, our answer can never be larger.

```python
def countBinarySubstringsGroup(self, s: str) -> int:
    groups = []
    prev = None
    for num in s:
        if prev==None or num!=prev:
            groups.append(1)
        else:
            groups[-1] += 1
        prev = num

    result = 0
    for i in range(len(groups)-1):
        result += min(groups[i], groups[i+1])

    return result
```

Time complexity is O(n):\
![image](https://user-images.githubusercontent.com/25105806/138643456-0c1a87af-7d3e-4ae9-ae0c-bf37502d0483.png)


<br />

### Approach 2: One Pass, countBinarySubstringsOnePass()
The idea is the same as approach 1 but since we only care about the adjacent two groups, we can only go over the list once and get the answer

```python
def countBinarySubstringsOnePass(self, s: str) -> int:
    result = 0
    pre = 0
    cur = 1
    for i in range(1, len(s)):
        if s[i-1] != s[i]:
            # for the first time s[i-1] != s[i], pre is 0, so the result is 0
            # which means a group of 0 or 1 does not contribute to any valid result
            result += min(pre, cur)
            pre, cur = cur, 1
        else:
            cur += 1

    return result + min(pre, cur)
```

As the gif animation shows:
![countBinarySubstr](https://user-images.githubusercontent.com/25105806/138643353-7fea895d-e192-4b6a-bf24-9d983ec0845c.gif)

Click [here](https://github.com/artisan1218/LeetCode-Solution/blob/main/countBinarySubtr/countBinarySubstr.ppsx) to download the animation.


Time complexity is O(n):\
![image](https://user-images.githubusercontent.com/25105806/138643506-b543e873-aef8-48d1-a273-ef52b9279283.png)


