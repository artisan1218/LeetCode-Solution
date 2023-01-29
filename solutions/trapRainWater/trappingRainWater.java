public class trappingRainWater {

    public static void main(String[] args) {
	// TODO Auto-generated method stub
	int[] height = new int[] { 0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1 };
	Solution solver = new Solution();

	System.out.println(solver.trapLevelByLevel(height));
    }

    private static class Solution {

	// TLE
	public int trapLevelByLevel(int[] height) {
	    int result = 0;

	    // get the tallest bar
	    // O(n)
	    int tallest = 0;
	    for (int bar : height) {
		if (bar > tallest) {
		    tallest = bar;
		}
	    }

	    // O(tallest) * O(n)
	    while (tallest > 0) {
		// get each level and compute volume of water level by level
		int volume = 0;
		int temp = 0;
		boolean first = true;
		// O(n)
		for (int bar : height) {
		    if (bar >= tallest) {
			// the bar is taller than current level, it is the boundary of a basin
			volume += temp;
			temp = 0;
			first = false;
		    } else {
			// the bar is shorter than current level, it can trap water
			// as long as it is not the first bar
			if (!first) {
			    temp += 1;
			}
		    }
		}
		tallest -= 1;

		// add volume of water at this level
		result += volume;
	    }

	    return result;
	}
    }
}
