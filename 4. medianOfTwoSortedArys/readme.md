# Find Median of Two Sorted Arrays problem
* Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.


### Approach 1: 
Since the two given arrays are sorted, we should utilize this sorted structure in that we only need to go through half of the total arrays and we can only store the median value upon reaching the middle point. There is no need to store all seen values and sort them for the second time. Main idea is to compare the smallest element of each array, skip the smaller one and check the next pair until reaching the middle point. Since we only go through half of the total array, the time complexity is simply O((m+n)/2), which is O(n)\
Turns out the running time is fairly good
![image](https://user-images.githubusercontent.com/25105806/117776937-f1af5880-b1f0-11eb-8868-eef6363e7aae.png)


### Approach 2:
