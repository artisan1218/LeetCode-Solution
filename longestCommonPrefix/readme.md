# Longest Common Prefix problem
* Write a function to find the longest common prefix string amongst an array of strings.
* If there is no common prefix, return an empty string `""`.


### Approach 1: longestCommonPrefix, Java
Since the common prefix is a substring that each string in `strs` will have, we can simply iterate through the `strs`, decide the common prefix pair by pair and keep the shortest one.\
![image](https://user-images.githubusercontent.com/25105806/118737282-5ffba880-b7f9-11eb-8f8d-ff5813dd8383.png)


### Approach 2: longestCommonPrefix, Python
We can easily and quickly decide the shortest string using `min()` function in python and check all chars at each string before the index of len of shortest string. E.g. if `ab` is the shortest string, then the common prefix must not exceed the length of 2, we can then check index 0 and index 1 for all strings to see if they are all equal.
![image](https://user-images.githubusercontent.com/25105806/118737572-f0d28400-b7f9-11eb-8f2a-42209dbfb7cc.png)
