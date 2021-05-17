# Longest Palindromic Substring problem
* Given a string `s`, return the longest palindromic substring in `s`.

### Approach 1: Brute Force, skipped
The obvious brute force solution is to pick all possible starting and ending positions for a substring, and verify if it is a palindrome.\
Finding all substrings of `s` uses O(n^2) time and verifying it uses O(n), so the final time complexity is O(n^3).

### Approach 2: Dynamic Programming, longestPalindromeMethodDP()
Basic idea of this approach is to go through the list of characters of string `s`, for each of the character in s, expand the candidate result to left and right one character a time until left and right are not equal, keep the intermediate result and compare it with the next candidate result and keep the longest one.\
<img src="https://user-images.githubusercontent.com/25105806/118064919-d9eee600-b350-11eb-8410-1a667e34b2ec.png" width="85%" height="85%">


Since we first go through the entire string, and for each character we expand at most len(s)/2 times, the worst case is when the entire string is a panlidorme, because we have to expand to both ends for each of the characters in the string and the time complexity is O(n^2).\
![image](https://user-images.githubusercontent.com/25105806/118066893-5df69d00-b354-11eb-87a6-7f89288afd1f.png)

### Approach 3: Improved Dynamic Programming, longestPalindromeMethodCleanDP()
The basic idea is the same as approach 2, but with improved data structure and logic structure. This solution has better readability.\
The time complexity is the same as approach 2, which is O(n^2), the actual running time is as follows:

![image](https://user-images.githubusercontent.com/25105806/118085398-35cc6580-b377-11eb-82a9-4da9c5bca99b.png)

We can see that it is indeed a little bit faster.


### Approach 4: Manacher's Algorithm, skipped
There is indeed a solution with linear time complexity, but since it is specific to this longest palindrome question and thus not an universal idea like dynamic programming, it is skipped due to complexity.
