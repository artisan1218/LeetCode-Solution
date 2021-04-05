# twoSum problem
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

### Approach 1: Brute force:
For each number in list, go through every other number in the list and test if they add up to target. Time complexity is O(n^2) 

### Approach 2: 
First build a HashMap that stores all number in the list, then iterate through the list to see if the target-num exists in the HashMap. Since HashMap has constant lookup time, it saves O(n), So fina time complexity is O(n), but use space complexity of O(n) to store the HashMap.
