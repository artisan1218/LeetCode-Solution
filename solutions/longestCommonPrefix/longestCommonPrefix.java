
public class longestCommonPrefix {

    public static void main(String[] args) {
	// TODO Auto-generated method stub
	String[] test = new String[] { "cir", "car" };
	System.out.println(longestCommonPrefix(test));

    }

    public static String longestCommonPrefix(String[] strs) {
	// since 1 <= strs.length <= 200, we can always set the first str to be the
	// longest common prefix at the very beginning
	String result = strs[0];

	for (int i = 1; i < strs.length; i++) {
	    String compStr = strs[i];
	    StringBuilder curr = new StringBuilder("");
	    String shorter = result.length() < compStr.length() ? result : compStr;

	    // compare each string with current result, decide their common prefix
	    for (int j = 0; j < shorter.length(); j++) {
		if (result.charAt(j) == compStr.charAt(j)) {
		    curr.append(shorter.charAt(j));
		} else {
		    break;
		}
	    }

	    // keep only the shortest common prefix
	    if (curr.length() < result.length()) {
		result = curr.toString();
	    }
	    if (result.length() == 0) {
		return "";
	    }
	}

	return result;
    }

}
