# Find Median of Two Sorted Arrays problem
* Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

Leetcode link: https://leetcode.com/problems/median-of-two-sorted-arrays/

<br/>

### Approach 1: Bruth Force, findMedianSortedArraysBruteForce()
Since the two given arrays are sorted, we should utilize this sorted structure in that we only need to go through half of the total arrays and we can only store the median value upon reaching the middle point. There is no need to store all seen values and sort them for the second time. Main idea is to compare the smallest element of each array, skip the smaller one and check the next pair until reaching the middle point. Since we only go through half of the total array, the time complexity is simply O((m+n)/2), which is O(n). This method is bruth force in that we will go through each of the element before the median.

```java
public static double findMedianSortedArraysBruteForce(int[] nums1, int[] nums2) {
	int sumLen = nums1.length + nums2.length;
	double median = 0;
	if (sumLen % 2 == 0) {
	    int medianPos1 = sumLen / 2 - 1;
	    int medianPos2 = sumLen / 2;
	    double median2 = 0;
	    int nums1Pos = 0;
	    int nums2Pos = 0;
	    for (int i = 0; i <= medianPos2; i++) {
		int comp1 = Integer.MAX_VALUE;
		int comp2 = Integer.MAX_VALUE;
		if (nums1Pos < nums1.length)
		    comp1 = nums1[nums1Pos];
		if (nums2Pos < nums2.length)
		    comp2 = nums2[nums2Pos];

		if (comp1 < comp2) {
		    nums1Pos++;
		    median = comp1;
		} else {
		    nums2Pos++;
		    median = comp2;
		}

		if (i == medianPos1) {
		    median2 = median;
		}
	    }
	    median += median2;
	    return median / 2;
	} else {
	    int medianPos = sumLen / 2;
	    int nums1Pos = 0;
	    int nums2Pos = 0;
	    for (int i = 0; i <= medianPos; i++) {
		int comp1 = Integer.MAX_VALUE;
		int comp2 = Integer.MAX_VALUE;
		if (nums1Pos < nums1.length)
		    comp1 = nums1[nums1Pos];
		if (nums2Pos < nums2.length)
		    comp2 = nums2[nums2Pos];

		if (comp1 < comp2) {
		    nums1Pos++;
		    median = comp1;
		} else {
		    nums2Pos++;
		    median = comp2;
		}
	    }
	    return median;
	}
    }
```

Turns out the running time is fairly good:\
![image](https://user-images.githubusercontent.com/25105806/117776937-f1af5880-b1f0-11eb-8868-eef6363e7aae.png)

<br/>

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


```java
public static double findMedianSortedArraysOptimal(int[] nums1, int[] nums2) {
	// make sure nums1 is the shorter array
	double median = 0;
	if (nums1.length <= nums2.length) {
	    int start = 0;
	    int end = nums1.length;
	    // if start == end, still need to enter the while loop because this might be the
	    // case where nums1 has a length of 0
	    while (start <= end) {
		// partition1 and partition2 is the position index at nums1 and nums2 where we
		// cut into two parts, such that length of left parts of nums1 and nums2 is
		// equal to length of right parts of nums1 and nums2 if the total length is odd,
		// then there is one less element in left than in right part

		// update the new partitions
		int partition1 = (start + end) / 2; // binary search
		int partition2 = (nums1.length + nums2.length) / 2 - partition1;

		// default value is min or max in case partition1 is 0, which means length of
		// left part is 0
		int maxLeft1 = (partition1 == 0) ? Integer.MIN_VALUE : nums1[partition1 - 1];
		int minRight1 = (partition1 == nums1.length) ? Integer.MAX_VALUE : nums1[partition1];
		// int minRight1 = nums1[partition1];

		// same logic for the partition of the second array
		int maxLeft2 = (partition2 == 0) ? Integer.MIN_VALUE : nums2[partition2 - 1];
		int minRight2 = (partition2 == nums2.length) ? Integer.MAX_VALUE : nums2[partition2];

		if (maxLeft1 <= minRight2 && maxLeft2 <= minRight1) {
		    // found the median!
		    if ((nums1.length + nums2.length) % 2 == 0) {
			// total length is even, can be cut evenly
			double left = Math.max(maxLeft1, maxLeft2);
			double right = Math.min(minRight1, minRight2);
			median = (left + right) / 2;
		    } else {
			// total length is odd, left part has one less element
			median = Math.min(minRight1, minRight2);
		    }
		    break;
		} else if (maxLeft1 <= minRight2 && maxLeft2 > minRight1) {
		    // partition1 is too left, should go to right
		    start = partition1 + 1;
		} else {
		    // partition1 is too right, should go to left
		    end = partition1 - 1;
		}
	    }
	    return median;
	} else {
	    return findMedianSortedArraysOptimal(nums2, nums1);
	}
    }
```

Time complexity is O(log(min(m,n))) thus O(log(n)) since we only check the shorter array and will do binary search on it, which will only look at most log(n) elements:\
![image](https://user-images.githubusercontent.com/25105806/118186874-1541f100-b3f3-11eb-925c-b1c4124f9d30.png)
