
public class jumpGame2 {

    public static void main(String[] args) {
	// TODO Auto-generated method stub
	int[] nums = new int[] { 0 };
	Solution solver = new Solution();
	System.out.println(solver.jumpGreedy2(nums));
    }

    static class Solution {
	public int jumpGreedy(int[] nums) {
	    if (nums.length == 1) {
		return 0;
	    } else {
		int jumps = 0;
		int i = 0;
		int farthest = 0;

		while (farthest + nums[i] < nums.length - 1) {
		    int max = 0;
		    // traverse through all jumping distances at this index
		    for (int j = 1; j <= nums[farthest]; j++) {
			// j+nums[farthest + j] because we have to consider the current index,
			// not just the max value of nums[farthest + j]
			// to solve case 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 0
			if (j + nums[farthest + j] >= max) {
			    max = j + nums[farthest + j];
			    i = farthest + j;
			}
		    }
		    jumps++;
		    farthest = i;
		}

		return jumps + 1;
	    }
	}

	public int jumpGreedy2(int[] nums) {

	    // defaults to 0 so we always jump once if the length of nums is greater than 0
	    int currJumpBoundary = 0;
	    int max = 0;
	    int jumps = 0;

	    for (int i = 0; i < nums.length - 1; i++) {
		// max is the farthest index that we can jump to from current index
		// we need to consider i+nums[i] instead of just nums[i]
		// similar to heuristic search
		max = Math.max(max, i + nums[i]);
		if (i == currJumpBoundary) {
		    currJumpBoundary = max;
		    jumps++;
		}
	    }
	    return jumps;
	}
    }
}
