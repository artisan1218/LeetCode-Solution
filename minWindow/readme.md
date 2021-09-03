# Minimum Window Substring problem
![image](https://user-images.githubusercontent.com/25105806/131955663-05e657db-aa89-4b42-a69b-889896c065af.png)


### Approach 1: Brute Force, minWindowBruteForce()
Find all substrings, test if it is valid and record the minimum length. Not surprisingly, lead to TLE.

### Approach 2: Two Pointers, minWindowTwoPointers()
Credits to: https://www.youtube.com/watch?v=jSto0O4AJbM

Use two pointers to bound the possible valid substring.

Acutal running time:\
![image](https://user-images.githubusercontent.com/25105806/131955882-0c3b197c-e704-4b6a-b8e3-dd4088a5b2ff.png)


    

