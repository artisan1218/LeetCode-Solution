# Longest Palindromic Substring problem
![image](https://user-images.githubusercontent.com/25105806/162558297-c2e550c4-40af-4ef0-8fa5-93a59faf32d6.png)

Leetcode link: https://leetcode.com/problems/longest-palindromic-substring/

<br />

### Approach 1: Brute Force, skipped
The obvious brute force solution is to pick all possible starting and ending positions for a substring, and verify if it is a palindrome.\
Finding all substrings of `s` uses O(n^2) time and verifying it uses O(n), so the final time complexity is O(n^3).

<br />

### Approach 2: Dynamic Programming, longestPalindromeMethodDP()
Basic idea of this approach is to go through the list of characters of string `s`, for each of the character in s, expand the candidate result to left and right one character a time until left and right are not equal, keep the intermediate result and compare it with the next candidate result and keep the longest one.\
<img src="https://user-images.githubusercontent.com/25105806/118064919-d9eee600-b350-11eb-8410-1a667e34b2ec.png" width="85%" height="85%">

```java
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
```

Since we first go through the entire string, and for each character we expand at most len(s)/2 times, the worst case is when the entire string is a panlidorme, because we have to expand to both ends for each of the characters in the string and the time complexity is O(n^2).\
![image](https://user-images.githubusercontent.com/25105806/118066893-5df69d00-b354-11eb-87a6-7f89288afd1f.png)

<br />

### Approach 3: Improved Dynamic Programming, longestPalindromeMethodCleanDP()
The basic idea is the same as approach 2, but with improved data structure and logic structure. This solution has better readability.


```java
public static String longestPalindromeMethodCleanDP(String s) {
	if (s.length() == 0) {
	    return "";
	} else {
	    int start = 0;
	    int end = 0;
	    // go through each character in the string s
	    for (int i = 0; i < s.length(); i++) {
		// the palindrome has odd length, expand around single point
		int oddLen = expand(s, i, i);
		// the palindrome has even length, expand around two points, here we assume that
		// i and i+1 are same character, because this won't affect the result and is
		// simple to implement
		int evenLen = expand(s, i, i + 1);
		int currLen = Math.max(oddLen, evenLen);
		// update the start and end index of the longest palindrome so far
		if (currLen > end - start) {
		    start = i - (currLen - 1) / 2;
		    end = i + currLen / 2;
		}
	    }
	    return s.substring(start, end + 1);
	}
    }

    public static int expand(String s, int leftCenter, int rightCenter) {
	// the radius of the expanding
	// leftExpPt means left expanding point, similarly for rightExpPt, they are
	// start at the center
	int leftExpPt = leftCenter, rightExpPt = rightCenter;
	while (leftExpPt >= 0 && rightExpPt < s.length() && s.charAt(leftExpPt) == s.charAt(rightExpPt)) {
	    leftExpPt--;
	    rightExpPt++;
	}
	return rightExpPt - leftExpPt - 1;
}
```


The time complexity is the same as approach 2, which is O(n^2), the actual running time is as follows:

![image](https://user-images.githubusercontent.com/25105806/118085398-35cc6580-b377-11eb-82a9-4da9c5bca99b.png)

We can see that it is indeed a little bit faster.

<br />

### Approach 4: Manacher's Algorithm, skipped
There is indeed a solution with linear time complexity, but since it is specific to this longest palindrome question and thus not an universal idea like dynamic programming, it is skipped due to complexity.
