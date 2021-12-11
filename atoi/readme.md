# String to Integer (atoi) problem
* Implement the `myAtoi(string s)` function, which converts a string to a 32-bit signed integer (similar to C/C++'s `atoi` function).
* The algorithm for myAtoi(string s) is as follows:
  1. Read in and ignore any leading whitespace.
  2. Check if the next character (if not already at the end of the string) is `'-'` or `'+'`. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
  3. Read in next the characters until the next non-digit charcter or the end of the input is reached. The rest of the string is ignored.
  4. Convert these digits into an integer (i.e. `"123" -> 123`, `"0032" -> 32`). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
  5. If the integer is out of the 32-bit signed integer range `[-2^31, 2^31 - 1]`, then clamp the integer so that it remains in the range. Specifically, integers less than `-2^31` should be clamped to `-2^31`, and integers greater than `2^31 - 1` should be clamped to `2^31 - 1`.
  6. Return the integer as the final result.

Leetcode link: https://leetcode.com/problems/string-to-integer-atoi/

<br />

### Approach 1: String Traversal, myAtoiNaive()
This approach is the native solution, which is easily to come up with, simply go through the string `s`, check each char and make corresponding actions.\

```java
public static int myAtoi(String s) {
	int result = 0;

	boolean firstIsSign = false;
	boolean beginAppendNum = false;
	boolean firstDot = false;

	// trim the leading white space
	String trimedStr = s.trim();
	StringBuilder resultStr = new StringBuilder("");

	for (int i = 0; i < trimedStr.length(); i++) {
	    char check = trimedStr.charAt(i);
	    if ((check == '-' || check == '+') && firstIsSign == false && beginAppendNum == false) {
		firstIsSign = true;
		resultStr.append(check);
	    } else if (Character.isDigit(check)) {
		beginAppendNum = true;
		resultStr.append(check);
	    } else if (check == '.' && firstDot == false) {
		firstDot = true;
		break;
	    } else if ((check < '0' || check > '9') && firstIsSign) {
		break;
	    } else if (i == 0 && (check < '0' || check > '9' || check != '-' || check != '+')) {
		return 0;
	    } else {
		break;
	    }
	}

	if (resultStr.length() == 0 || (firstIsSign && resultStr.length() == 1)) {
	    return 0;
	}

	try {
	    result = Integer.parseInt(resultStr.toString());
	} catch (Exception e) {
	    return resultStr.charAt(0) == '-' ? Integer.MIN_VALUE : Integer.MAX_VALUE;
	}

	return result;
    }
```

Time complexity is simply O(n) because we only visit each of the chars in the string `s` once.\
![image](https://user-images.githubusercontent.com/25105806/118205932-63b4b700-b416-11eb-9dd8-32adf6f0119d.png)

### Approach 2: DFA(Deterministic Finite Automaton), myAtoiDFA()
Credits to: https://leetcode.com/problems/string-to-integer-atoi/discuss/798380/Fast-and-simpler-DFA-approach-(Python-3)

This approach utilizes the DFA to implement the logic behind this question. Turns out we can use three states to represent the logic of this question:
1. Space state, which can go to Space, Digit, or Sign state. If the current char is not `' '`, not `'+'` or `'-'` and not a digit, should simply return 0(reject state)
2. Sign state, which can only to go Digit state. If current char is not digit, simply return 0(reject state)
3. Digit state, which can only go to Digit state. If current char is not a digit, return the current value(reject state)

We will still go through each char of the string `s`, then decide which state to go depends on the value of `s` and the current state.\
The DFA is shown below:\
<img src="https://user-images.githubusercontent.com/25105806/118206316-16851500-b417-11eb-97ae-82cfea4b4f8a.png" height="70%" width="70%">


```java
public static int myAtoiDFA(String s) {
	boolean isNeg = false;
	String state = "space";
	int result = 0;
	for (int i = 0; i < s.length(); i++) {
	    char currChar = s.charAt(i);
	    switch (state) {
	    case "space":
		if (currChar == ' ') { // if next char is space, still go to space state
		    state = "space";
		} else if (currChar == '+' || currChar == '-') { // go to sign state
		    state = "sign";
		    isNeg = currChar == '-' ? true : isNeg;
		} else if (Character.isDigit(currChar)) { // go to digit state
		    state = "digit";
		    // add to result
		    result = result * 10 + Integer.parseInt(String.valueOf(currChar));
		} else {
		    // if the currChar is not space, not sign and not digit, should simply return 0
		    return 0;
		}
		break;
	    case "sign":
		if (Character.isDigit(currChar)) { // go to digit state
		    state = "digit";
		    // add to result
		    result = result * 10 + Integer.parseInt(String.valueOf(currChar));
		} else {
		    // if currChar is not digit, simply return 0
		    return 0;
		}
		break;
	    case "digit":
		if (Character.isDigit(currChar)) {
		    state = "digit";
		    // either the current result is bigger than MAX_VALUE/10, which means next value
		    // must exceed the integer limit, or the current result is exactly 1/10 of
		    // MAX_VALUE, but the next digit is bigger than the least digit of MAX_VALUE,
		    // which means the next value will also be greater than the integer limit.
		    if (result > Integer.MAX_VALUE / 10 || (result == Integer.MAX_VALUE / 10
			    && Integer.parseInt(String.valueOf(currChar)) > Integer.MAX_VALUE % 10)) {
			return isNeg ? Integer.MIN_VALUE : Integer.MAX_VALUE;
		    }
		    result = result * 10 + Integer.parseInt(String.valueOf(currChar));
		} else {
		    // is currChar is not char, return the current value
		    return isNeg ? -result : result;
		}
	    }
	}
	return isNeg ? -result : result;
    }
```

Time complexity is also O(n) because we only visit each of the chars in the string `s` once.\
![image](https://user-images.githubusercontent.com/25105806/118206818-251ffc00-b418-11eb-97b4-741c4fa944d3.png)


