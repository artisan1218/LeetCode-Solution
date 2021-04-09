import java.util.HashMap;
import java.util.Map;

public class LongestSubstringWithoutRepeatingChar {

    public static void main(String[] args) {
	String testStr = "tmmzuxt";
	System.out.println(lengthOfLongestSubstring(testStr));

    }

    public static int lengthOfLongestSubstring(String s) {
	int longestLen = 0;
	int currLen = 0;
	int left = 0; // left pointer
	int right = 0; // right pointer
	// map that keeps track of each char and the corresponding index
	Map<Character, Integer> charIdxMap = new HashMap<>();
	for (right = 0; right < s.length(); right++) {
	    // get the current char
	    char currChar = s.charAt(right);
	    if (!charIdxMap.containsKey(currChar)) { // new char
		// if this is a new char, simply increment the current length
		currLen++;
	    } else {
		// not a new char, then update the position of left pointer
		// so that the left and right form a proper window in which each char is unique
		// do not need to remove char that are not in the current window from the map
		// simply compare the index with left, if index is smaller, then the window does
		// not include that char, otherwise update left to the char's index
		left = Math.max(charIdxMap.get(currChar) + 1, left);
		currLen = right - left + 1;
	    }
	    // update the map with new char's index or add a new char-index pair
	    charIdxMap.put(currChar, right);
	    longestLen = Math.max(currLen, longestLen);
	}
	return longestLen;
    }

}
