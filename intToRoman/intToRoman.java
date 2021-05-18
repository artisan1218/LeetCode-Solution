
public class intToRoman {

    public static void main(String[] args) {
	// TODO Auto-generated method stub
	System.out.println(intToRomanMath2(999));

    }

    public static String intToRomanMath2(int num) {
	int[] values = { 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 };
	String[] symbols = { "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" };
	StringBuilder result = new StringBuilder();

	for (int i = 0; i < values.length; i++) {
	    while (num >= values[i]) {
		num -= values[i];
		result.append(symbols[i]);
	    }
	}
	return result.toString();
    }

    public static String intToRomanMath(int num) {
	String M[] = { "", "M", "MM", "MMM" };
	String C[] = { "", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM" };
	String X[] = { "", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC" };
	String I[] = { "", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX" };
	return M[num / 1000] + C[(num % 1000) / 100] + X[(num % 100) / 10] + I[num % 10];
    }

    public static String intToRomanLoop(int num) {
	String one = "I", five = "V", ten = "X", fifty = "L", hundred = "C", fiveHundred = "D", thousand = "M";
	String result = "";

	// fold is the multiple that we're currently dealing with, ranges from 1, 10,
	// 100, etc
	int fold = 1;
	while (num != 0) {
	    int digit = num % 10;
	    if (digit > 0 && digit < 4) { // I, II, III
		for (int i = 0; i < digit; i++) {
		    switch (fold) {
		    case 1:
			result = one + result;
			break;
		    case 10:
			result = ten + result;
			break;
		    case 100:
			result = hundred + result;
			break;
		    case 1000:
			result = thousand + result;
			break;
		    }
		}
	    } else if (digit == 4) {
		switch (fold) {
		case 1:
		    result = one + five + result;
		    break;
		case 10:
		    result = ten + fifty + result;
		    break;
		case 100:
		    result = hundred + fiveHundred + result;
		    break;
		}
	    } else if (digit > 4 && digit < 9) { // 5, 6, 7, 8
		String tmp = "";
		switch (fold) {
		case 1:
		    tmp = five;
		    break;
		case 10:
		    tmp = fifty;
		    break;
		case 100:
		    tmp = fiveHundred;
		    break;
		}
		for (int i = 0; i < digit - 5; i++) {
		    switch (fold) {
		    case 1:
			tmp = tmp + one;
			break;
		    case 10:
			tmp = tmp + ten;
			break;
		    case 100:
			tmp = tmp + hundred;
			break;
		    case 1000:
			tmp = tmp + thousand;
			break;
		    }
		}

		result = tmp + result;

	    } else if (digit == 9) {
		switch (fold) {
		case 1:
		    result = one + ten + result;
		    break;
		case 10:
		    result = ten + hundred + result;
		    break;
		case 100:
		    result = hundred + thousand + result;
		    break;
		}
	    }

	    num /= 10;
	    fold *= 10;
	}

	return result;
    }

}
