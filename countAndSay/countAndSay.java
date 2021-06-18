
public class countAndSay {

    public static void main(String[] args) {
	// TODO Auto-generated method stub
	Solution solver = new Solution();
	System.out.println(solver.countAndSay(6));
    }

    private static class Solution {
	public String countAndSay(int n) {
	    if (n == 1) {
		return "1";
	    }
	    StringBuilder result = new StringBuilder("1");
	    for (int i = 1; i < n; i++) {
		result = count(result);
	    }
	    return result.toString();
	}

	public StringBuilder count(StringBuilder str) {
	    StringBuilder res = new StringBuilder("");
	    int count = 1;
	    char digit = str.charAt(0);
	    for (int i = 1; i < str.length(); i++) {
		char check = str.charAt(i);
		if (check == digit) {
		    count++;
		} else {
		    res.append(String.valueOf(count) + String.valueOf(digit));
		    digit = check;
		    count = 1;
		}
	    }
	    res.append(String.valueOf(count) + String.valueOf(digit));
	    return res;
	}
    }

}
