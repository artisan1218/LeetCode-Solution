
public class atoi {

    public static void main(String[] args) {
	// TODO Auto-generated method stub
	System.out.println(myAtoiDFA("987 a"));
    }

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

}
