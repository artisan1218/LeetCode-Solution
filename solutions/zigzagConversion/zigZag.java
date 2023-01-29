
public class zigZag {
    public static void main(String[] args) {
	// TODO Auto-generated method stub
	System.out.print(convert("abcabcabcabcabc", 6));
    }

    public static String convert(String s, int numRows) {
	if (numRows == 1) {
	    return s;
	} else {
	    StringBuilder result = new StringBuilder("");
	    int row = 0;
	    // skippedNum is the number of chars that we need to skip in order to get the
	    // string in line-by-line order if the string is printed in zigzag order
	    int skippedNum = 2 * numRows - 2;
	    int i = 0;
	    // skippedBottom is the number of chars that we need to skip at the bottom part
	    // of the zigzag shaped string (v shape), while skippedTop is the number of
	    // chars that we need to skip at the top part of the zigzag shaped string (^
	    // shape).
	    int skippedBottom = skippedNum;
	    int skippedTop = 0;
	    boolean switch2Bottom = true;

	    while (row < numRows) {
		i = row; // i starts at the row index, which is the first char in that row
		switch2Bottom = true;
		if (row == 0 || row == numRows - 1) {
		    while (i < s.length()) {
			result.append(s.charAt(i));
			i += skippedNum;
		    }
		} else {
		    skippedBottom -= 2;
		    skippedTop += 2;
		    while (i < s.length()) {
			result.append(s.charAt(i));
			// switching between these two different skipped number we can control the pace
			// of i, which controls chars to be appended
			if (switch2Bottom) {
			    i += skippedBottom;
			    switch2Bottom = false;
			} else {
			    i += skippedTop;
			    switch2Bottom = true;
			}
		    }
		}
		row++;
	    }
	    return result.toString();
	}

    }
}
