
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

    public static String solution(String[] strs) {
	String result = "";
	boolean same = true;
	for (int i = 0; same; i++) {
	    for (int j = 0; j < strs.length - 1; j++) {
		String word = strs[j];
		String nextWord = strs[j + 1];
		if (i >= word.length() || i >= nextWord.length()) {
		    same = false;
		} else {
		    same = same && (word.charAt(i) == nextWord.charAt(i));
		}
	    }

	    if (strs.length == 0) {
		same = false;
	    } else if (strs.length == 1) {
		result = strs[0];
		same = false;
	    }
	    if (same) {
		result = result + strs[0].charAt(i);
	    }
	}

	return result;
    }

}
