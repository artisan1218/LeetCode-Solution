# Valid Palindrome problem
![image](https://user-images.githubusercontent.com/25105806/153356996-2467fdb6-3093-44fb-b228-cef390798ea4.png)

Leetcode link: https://leetcode.com/problems/valid-palindrome/

<br/>

### Approach 1: Two Pointers, isPalindrome()
Compared to standard palindrome validation question, the difference is that we now have to consider alphanumeric characters instead of only letters. Simply use the built-in function `.isalnum()` to test if its legal a character then compare the front character with back character.

```python3
def isPalindrome(self, s: str) -> bool:
    front, back = 0, len(s)-1
    while front < back:
        if not s[front].isalnum():
            front += 1
            continue # go directly to the next iteration without checking equality
        if not s[back].isalnum():
            back -= 1
            continue # go directly to the next iteration without checking equality

        if s[front].lower() == s[back].lower():
            front += 1
            back -= 1
        else:
            return False
    return True
```

Time complexity is O(n) and space complexity is O(1):\
![image](https://user-images.githubusercontent.com/25105806/153357460-eb0fb40a-ae2c-4e02-9737-d5f488ee56bc.png)
