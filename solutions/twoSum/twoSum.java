import java.util.HashMap;
import java.util.Map;

public class twoSum {

    public static void main(String[] args) {
	// TODO Auto-generated method stub
	int[] test = new int[] { 2, 7, 11, 15 };
	int[] result = hashMapOnePass(test, 9);
	for (int i = 0; i < result.length; i++) {
	    System.out.print(result[i] + " ");
	}
    }

    public static int[] hashMapOnePass(int[] nums, int target) {
	HashMap<Integer, Integer> map = new HashMap<>();
	int[] result = new int[2];

	for (int i = 0; i < nums.length; i++) {
	    int addend = nums[i];
	    int complement = target - addend;
	    if (map.containsKey(complement)) {
		result[0] = map.get(complement);
		result[1] = i;
		return result;
	    } else {
		map.put(addend, i);
	    }
	}

	return result;
    }

    public static int[] bruteForce(int[] nums, int target) {
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

    public static int[] hashMapTwoPass(int[] nums, int target) {

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
