# Length of Last Word problem
* Given a string `s` consists of some words separated by spaces, return the length of the last word in the string. If the last word does not exist, return `0`.
* A **word** is a maximal substring consisting of non-space characters only.

Leetcode link: https://leetcode.com/problems/length-of-last-word/

<br />

### Approach 1: Trim Trailing White Spaces and Split, lengthOfLastWordStripAndSplit()
Since a word is considered as non-space characters only, we cannot directly use `.split(' ')` function to split the word because for `s='a '`, there will be an empty character `''` at the end. Instead, use `.strip()` function to remove any white spaces at the end of `s` and then split, then return the length of the last word. We can use `rstrip()` to only remove the white spaces at the right side of `s` since we will only deal with trailing white spaces. 

```python3
def lengthOfLastWordStripAndSplit(self, s: str) -> int:
    return len(s.strip().split(' ')[-1])
```

Time complexity is O(n):

![c5755379fa949bbf45b3abeb708dbe7](https://user-images.githubusercontent.com/25105806/127754356-35af67b4-fe77-4e88-9b33-cc45699262fa.png)

<br />

### Approach 2: Looping, lengthOfLastWordLoop()
The idea is same as approach 1 but we use loop to achieve it instead. Start from the end, count only non-space characters until we meet a space that marks the end of last word.

```python3
def lengthOfLastWordLoop(self, s: str) -> int:
    result = 0
    for char in reversed(s):
        if char!=' ':
            result+=1
        elif result>0:
            return result
    return result
```

Time complexity is O(n):

![c5755379fa949bbf45b3abeb708dbe7](https://user-images.githubusercontent.com/25105806/127754356-35af67b4-fe77-4e88-9b33-cc45699262fa.png)
