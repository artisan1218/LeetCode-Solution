
public class longestPalindrome {

    public static void main(String[] args) {
	// TODO Auto-generated method stub
	System.out.println(longestPalindromeMethodBruteForce("bccbad"));
    }

    public static String longestPalindromeMethodBruteForce(String s) {
	String longestPan = "";
	String currPand = "";
	String candPanOdd = "";
	String candPanEven = "";

	if (s.length() == 1) {
	    return s;
	} else {
	    for (int i = 0; i < s.length() - 1; i++) {
		int left = 1;
		int right = 1;
		// initial value
		candPanOdd = s.substring(i, i + 1);

		// Check for palindrome of odd length
		while (i - left >= 0 && i + right < s.length()) {
		    // if the left element and right element revolving the middle element is the
		    // same, we expand
		    if (s.charAt(i - left) == s.charAt(i + right)) {
			candPanOdd = s.substring(i - left, i + right + 1);
			left++;
			right++;
		    } else {
			break;
		    }
		}

		// Check for even length palindorme
		if (s.charAt(i) == s.charAt(i + 1)) {
		    left = 1;
		    right = 2;
		    // initial value is the middle two char of the even length palindorme
		    candPanEven = s.substring(i, i + 2);
		    while (i - left >= 0 && i + right < s.length()) {
			if (s.charAt(i - left) == s.charAt(i + right)) {
			    candPanEven = s.substring(i - left, i + right + 1);
			    left++;
			    right++;
			} else {
			    break;
			}
		    }
		}

		currPand = (candPanOdd.length() > candPanEven.length()) ? candPanOdd : candPanEven;

		if (currPand.length() > longestPan.length()) {
		    longestPan = currPand;
		}
	    }
	}

	return longestPan;
    }

}
