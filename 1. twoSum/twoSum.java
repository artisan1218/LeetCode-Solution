import java.util.HashMap;
import java.util.Map;

public class twoSum {

    public static void main(String[] args) {
	// TODO Auto-generated method stub
	int[] test = new int[] { 1, 2, 3, 4, 5, 6, 7, 8, 9 };
	int[] result = twoSumSol(test, 5);
	for (int i = 0; i < result.length; i++) {
	    System.out.print(result[i] + " ");
	}
    }

    public static int[] twoSumSol(int[] nums, int target) {
	int[] result = new int[2];
	int addend = 0;
	int addendIt = 0;
	boolean find = false;
	for (int i = 0; i < nums.length && !find; i++) {
	    addend = nums[i];
	    for (int j = i + 1; j < nums.length && !find; j++) {
		addendIt = nums[j];
		if (addend + addendIt == target) {
		    result[0] = i;
		    result[1] = j;
		    find = true;
		}
	    }
	}
	return result;
    }

    public static int[] twoSumQuick(int[] nums, int target) {

	Map<Integer, Integer> s = new HashMap<>();
	for (int i = 0; i < nums.length; i++) {
	    s.put(nums[i], i);
	}

	for (int j = 0; j < nums.length; j++) {
	    int complement = target - nums[j];
	    if (s.containsKey(complement) && s.get(complement) != j) {
		return new int[] { j, s.get(complement) };
	    }
	}

	return null;
    }

}
