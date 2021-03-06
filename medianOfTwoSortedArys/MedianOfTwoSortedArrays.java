public class MedianOfTwoSortedArrays {

    public static void main(String[] args) {
	// TODO Auto-generated method stub

	int[] nums1 = { 1, 2 };
	int[] nums2 = { 3, 4 };

	System.out.println(findMedianSortedArraysOptimal(nums1, nums2));
    }

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

	// return median;
    }

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
}
