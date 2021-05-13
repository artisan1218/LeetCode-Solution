# Find Median of Two Sorted Arrays problem
* Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.


### Approach 1: Bruth Force, findMedianSortedArraysBruteForce()
Since the two given arrays are sorted, we should utilize this sorted structure in that we only need to go through half of the total arrays and we can only store the median value upon reaching the middle point. There is no need to store all seen values and sort them for the second time. Main idea is to compare the smallest element of each array, skip the smaller one and check the next pair until reaching the middle point. Since we only go through half of the total array, the time complexity is simply O((m+n)/2), which is O(n). This method is bruth force in that we will go through each of the element before the median.\
Turns out the running time is fairly good

![image](https://user-images.githubusercontent.com/25105806/117776937-f1af5880-b1f0-11eb-8868-eef6363e7aae.png)


### Approach 2: Binary Search, findMedianSortedArraysOptimal()
Algorithm credits to https://www.youtube.com/watch?v=LPFhl65R7ww

The main idea is to cut the arrays into two partitions, each partition will have two parts: array1 part and array2 part. Find the correct partitions such that: 
1. Sum of the length of left parts of the two arrays is equal to that of the right parts of the two arrays
2. Max value of the left part of array1 is less than min value of the right part of array2 and max value of left part of array2 is less than min value of right part of array1

We will encounter two situations when doing binary search:
1. Max value of the left part of array1 is greater than min value of the right part of array2, which means the partition of array1 is at too left side and we should move it to right. We apply binary search here and adjust the new partition to be equal to (old partition + 1 + right bound)/2.
2. Max value of the left part of the array2 is greater than min value of the right part of array1, which means the partition of array 1 is at too right side and we should move it to left. We apply binary search here and adjust the new partition to be equal to (left bound + old partition - 1)/2.

Example:\
 <img src="https://user-images.githubusercontent.com/25105806/117905246-bc097e80-b287-11eb-8b0d-c1fdbcf3e072.png" width="85%" height="85%">

Time complexity is O(log(min(m,n))) thus O(log(n)) since we only check the shorter array and will do binary search on it, which will only look at most log(n) elements

![image](https://user-images.githubusercontent.com/25105806/118186874-1541f100-b3f3-11eb-925c-b1c4124f9d30.png)
