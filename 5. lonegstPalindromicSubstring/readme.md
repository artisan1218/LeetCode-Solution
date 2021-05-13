# Longest Palindromic Substring problem
* Given a string `s`, return the longest palindromic substring in `s`.


### Approach 1: Bruth Force, longestPalindromeMethodBruteForce()
Basic idea of this approach is to go through the list of characters of string `s`, for each of the character in s, expand the candidate result to left and right one character a time until left and right are not equal, keep the intermediate result and compare it with the next candidate result and keep the longest one.\
<img src="https://user-images.githubusercontent.com/25105806/118064919-d9eee600-b350-11eb-8410-1a667e34b2ec.png" width="85%" height="85%">\
Since we first go through the entire string, and for each character we expand at most len(s)/2 times, the worst case is when the entire string is a panlidorme, because we have to expand to both ends for each of the characters in the string and the time complexity is O(n^2).\
The running time is indeed quite slow compare to optimal solution.
![image](https://user-images.githubusercontent.com/25105806/118064081-33561580-b34f-11eb-836a-7002856a8fd9.png)

### Approach 2:
