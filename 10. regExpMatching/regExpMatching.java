
public class regExpMatching {

    public static void main(String[] args) {
	// TODO Auto-generated method stub
	System.out.println(isMatchDP("aaa", "a*a"));
    }

    public static boolean isMatchDP(String s, String p) {
	// match matrix has length s.length()+1 and p.length()+1 to deal with empty p
	// and empty s, default value is false
	boolean match[][] = new boolean[s.length() + 1][p.length() + 1];

	match[0][0] = true; // empty pattern matches empty string

	// first column is all false except for match[0][0], no need to initialize since
	// default is false, only need to initialize values of the first row
	for (int column = 1; column < p.length() + 1; column++) {
	    // index of p starts at 0, which is the first char of p
	    // if a char of p is *, then check the char two indices before *, if that char
	    // in match is true, then the current column is also true because that's saying
	    // adding this Kleene star operation does not affect the matching
	    // e.g. if "abc" matches a string, then "abcd*" still matches that string
	    match[0][column] = p.charAt(column - 1) == '*' && match[0][column - 2];
	}

	// start the real algorithm
	// go through the matrix row by row
	for (int row = 1; row < s.length() + 1; row++) {
	    // fill in the matrix column by column for each row
	    for (int column = 1; column < p.length() + 1; column++) {
		if (s.charAt(row - 1) == p.charAt(column - 1) || p.charAt(column - 1) == '.') {
		    // case no.1: the new char in s and p are the same or the char in p is a dot,
		    // which means adding this char does not change the current result, then simply
		    // assign the value at position (row, column) to be the value at position
		    // (row-1, column-1) because (row-1, column-1) stands for not adding this char
		    // e.g. for s="abc" and p="ab*c", if s[2]==p[3], which means c==c, then the
		    // value only depends on if "ab*" matches "ab"
		    match[row][column] = match[row - 1][column - 1];
		} else if (p.charAt(column - 1) == '*') {
		    // case no.2: the new char in p is a kleene star. We have two sub cases here:
		    // if the char* is considered as empty, is the result true?
		    // if the char* is considered once or more times, is the result true?
		    if (match[row][column - 2] == true) {
			// can be considered as empty
			// e.g. for s="a" and p="a*b*", if "a*" matches "a", then "a*b*" also matches
			// "a". Adding "b*" does not change the result
			match[row][column] = true;
		    } else if (s.charAt(row - 1) == p.charAt(column - 2) || p.charAt(column - 2) == '.') {
			// the char before * in p is equal to s at row-1 (the current s char)
			// or the char before * is a kleene star, which matches any char
			// e.g. for s="ab", p="ab*", "a" alone does not match "ab". s[2-1]==p[3-2]=="b",
			// so the value only depends on whether "ab*" maches "a"
			match[row][column] = match[row - 1][column];
		    }
		}
		// case no.3: the new char in s and p are not the same, the value will be false,
		// which is default value, so no need to explicitly assign

	    }
	}

	return match[s.length()][p.length()];
    }
}
