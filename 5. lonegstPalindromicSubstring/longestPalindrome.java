
public class longestPalindrome {

    public static void main(String[] args) {
	// TODO Auto-generated method stub
	System.out.println(longestPalindromeMethodDP("bccbcd"));
    }

    public static String longestPalindromeMethodDP(String s) {
	String longestPan = "";
	String currPand = "";

	if (s.length() == 1) {
	    return s;
	} else {
	    for (int i = 0; i < s.length() - 1; i++) {
		int left = 1;
		int right = 1;
		// initial value
		int oddCandLeft = i;
		int oddCandRight = i + 1;
		// candPanOdd = s.substring(i, i + 1);

		// Check for palindrome of odd length
		while (i - left >= 0 && i + right < s.length()) {
		    // if the left element and right element revolving the middle element is the
		    // same, we expand
		    if (s.charAt(i - left) == s.charAt(i + right)) {
			oddCandLeft = i - left;
			oddCandRight = i + right + 1;
			left++;
			right++;
		    } else {
			break;
		    }
		}

		int evenCandLeft = 0;
		int evenCandRight = 0;
		// Check for even length palindorme
		if (s.charAt(i) == s.charAt(i + 1)) {
		    evenCandLeft = i;
		    evenCandRight = i + 2;
		    left = 1;
		    right = 2;
		    // initial value is the middle two char of the even length palindorme
		    while (i - left >= 0 && i + right < s.length()) {
			if (s.charAt(i - left) == s.charAt(i + right)) {
			    evenCandLeft = i - left;
			    evenCandRight = i + right + 1;
			    left++;
			    right++;
			} else {
			    break;
			}
		    }
		}

		// pick the longest candidates, right-left is the length of the candidate
		// palindrome
		if ((oddCandRight - oddCandLeft) > (evenCandRight - evenCandLeft)) {
		    currPand = s.substring(oddCandLeft, oddCandRight);
		} else {
		    currPand = s.substring(evenCandLeft, evenCandRight);
		}

		if (currPand.length() > longestPan.length()) {
		    longestPan = currPand;
		}
	    }
	}

	return longestPan;
    }

}
