public class medianTwoSortedArrays {

    public static void main(String[] args) {
	// TODO Auto-generated method stub

	int[] nums1 = { 1, 2, 4 };
	int[] nums2 = { 3, 4, 5 };

	System.out.println(findMedianSortedArrays(nums1, nums2));
    }

    public static double findMedianSortedArrays(int[] nums1, int[] nums2) {
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
