# Remove Duplicates from Sorted Array problem
* Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.
* Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

### Approach 1: Two Pointers, removeDuplicates()
The key point is that the given array `nums` is sorted in ascending order. We can use two pointers, one fast mover and one slow mover, to check the elements from left to right. The slow mover `modifier` is to modify the element in the array `nums` so that the array contains only unique elements. The fast mover `cursor` is to read every elements and check if the element is already added.\
We will only read the array once, so the time complexity is O(n)

![image](https://user-images.githubusercontent.com/25105806/120942324-13f7a180-c6dd-11eb-9281-49715af99163.png)
