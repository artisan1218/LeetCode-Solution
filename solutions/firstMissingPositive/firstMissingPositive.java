import java.util.HashSet;
import java.util.Set;

public class firstMissingPositive {

    public static void main(String[] args) {
	// TODO Auto-generated method stub
	int[] nums = { 2, 1, 7, 8, 9, 11, 12 };
	Solution solver = new Solution();
	System.out.println(solver.firstMissingPositiveInplaceHashing(nums));

    }

    private static class Solution {

	public int firstMissingPositiveInplaceHashing(int[] nums) {

	    int len = nums.length;

	    // if a number is < 0 or > len, we can replace it with a special number len + 1
	    // the number is impossible to be the answer. The answer must be within the
	    // range 1 and len + 1
	    for (int i = 0; i < len; i++) {
		if (nums[i] <= 0 || nums[i] > len) {
		    nums[i] = len + 1;
		}
	    }

	    for (int i = 0; i < len; i++) {
		// take abs value of any number read to compare it with the len
		int num = Math.abs(nums[i]);
		// is a number is smaller or equal to len, it will be in the range of 1 to len +
		// 1
		if (num <= len) {
		    // then convert it to zero index based array
		    // e.g. 2 will be placed at index 1 if the array is continues
		    num--;
		    // if the 0-based index has a pos number, we convert it to neg number to mark it
		    // as "exist"
		    if (nums[num] > 0) { // prevents double negative operations
			// convert it to neg because it keeps the magnitude of the original number
			// we can simply restore its original value and compare it with len by taking
			// abs value of it
			nums[num] = -1 * nums[num];
		    }
		}
	    }

	    // the first number whose positive will be the answer because we've replaced any
	    // existing number in range 1 to len + 1 with neg value at it's corresponding
	    // index as if the array is continues
	    for (int i = 0; i < len; i++) {
		if (nums[i] >= 0) {
		    return i + 1;
		}
	    }

	    // every number is within the range of 1 to len + 1, simply return len + 1,
	    // which is the next number
	    return len + 1;
	}

	/**
	 * O(n) but not constant extra space
	 */
	public int firstMissingPositiveHashSet(int[] nums) {
	    // cache the nums using HashSet
	    Set<Integer> existence = new HashSet<>();
	    for (int num : nums) {
		existence.add(num);
	    }
	    // checking for non-existing least positive integer
	    for (int i = 1; true; i++) {
		if (!existence.contains(i)) {
		    return i;
		}
	    }
	}
    }

}
