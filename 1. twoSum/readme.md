# twoSum problem
* Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
* You may assume that each input would have exactly one solution, and you may not use the same element twice.
* You can return the answer in any order.

### Approach 1: Brute force, bruteForce()
For each number in list, go through every other number in the list and test if they add up to target. Time complexity is O(n^2) 

### Approach 2: twoPassHashMap()
First build a HashMap that stores all number in the list, then iterate through the list to see if the target-num(complement) exists in the HashMap. Since HashMap has constant lookup time, it saves O(n), So fina time complexity is O(n), but use space complexity of O(n) to store the HashMap.

### Approach 3: onePassHashMap()
Turns out we can check if the complement exists in the HashMap while building the HashMap. HashMap is the element:index pair of the list. Iterate through the list, if the HashMap contains the complement, then we've found the answer, simply return the current index and the index of the complement; if the HashMap does not contain the complement, then adding this number and its index to the HashMap. Since the HashMap has contant lookup time, the overall time complexity is O(n) and space complexity is O(n). Best case is when the two numbers are the first two elements of the list, which will be returned when we get the second element because now the complement is the first element and it's in the HashMap already. Worst case is when either one of the two numbers is at the end of the list, which will not be found until we reach the end.
