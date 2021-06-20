import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class combinationSum {

    public static void main(String[] args) {
	// TODO Auto-generated method stub
	Solution solver = new Solution();
	int[] nums = { 1, 2, 3, 6 };
	int target = 3;

	// List<List<Integer>> result = solver.combinationSumBacktrack(nums, target);
	List<List<Integer>> result = solver.combinationSumDP(nums, target);
	System.out.println(result);

    }

    static class Solution {

	public List<List<Integer>> combinationSumDP(int[] candidates, int target) {
	    List<List<List<Integer>>> dp = new ArrayList<>();

	    // currTarget begins at 1 because the condition 1 <= target <= 500
	    for (int currTarget = 1; currTarget <= target; currTarget++) {
		List<List<Integer>> row = new ArrayList<>();
		// go over the candidates that we can choose digit from
		for (int digit : candidates) {
		    // if a digit is smaller than the current target, we can add it to current
		    // combination and looking back for the remaining numbers by checking dp
		    if (digit < currTarget) {
			for (List<Integer> prevAns : dp.get(currTarget - digit - 1)) {
			    // to avoid duplicates
			    if (digit <= prevAns.get(0)) {
				List<Integer> combination = new ArrayList<>();
				combination.add(digit);
				combination.addAll(prevAns);
				row.add(new ArrayList<>(combination));
			    }
			}
		    } else if (digit == currTarget) {
			// case when a single digit is equal to target
			List<Integer> combination = new ArrayList<>();
			combination.add(digit);
			// add a new copy of the combination so that it will not be changed
			row.add(new ArrayList<>(combination));
		    }
		}
		dp.add(new ArrayList<>(row));
	    }

	    return dp.get(target - 1);
	}

	public List<List<Integer>> combinationSumBacktrack(int[] candidates, int target) {
	    List<List<Integer>> result = new ArrayList<>();
	    List<Integer> combination = new ArrayList<>();
	    int sum = 0;

	    backtrack(candidates, target, result, combination, sum);
	    // this is to remove duplicates combinations
	    Set<List<Integer>> unique = new HashSet<>();
	    for (List<Integer> comb : result) {
		Collections.sort(comb);
		unique.add(comb);
	    }
	    return new ArrayList<>(unique);
	}

	public boolean backtrack(int[] candidates, int target, List<List<Integer>> result, List<Integer> combination,
		int sum) {

	    // go over each digit in the list
	    for (int digit : candidates) {
		if ((sum + digit) < target) {
		    // if adding the current digit does not exceed the target, we can add it safely
		    combination.add(digit);
		    sum += digit;
		    // keeping checking the rest of the digit until an adding exceeds the target
		    // or all digits are seen
		    if (!backtrack(candidates, target, result, combination, sum)) {
			// an adding is not successful, start backtracking by removing the current digit
			sum -= digit;
			combination.remove(combination.size() - 1);
		    }
		} else if ((sum + digit) == target) {
		    // we've found a combination, add the combination to result and check the next
		    // digit
		    combination.add(digit);
		    result.add(new ArrayList<>(combination));
		    combination.remove(combination.size() - 1);
		}
	    }
	    return false;
	}
    }
}
