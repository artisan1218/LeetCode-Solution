
public class divideTwoInts {

    public static void main(String[] args) {
	// TODO Auto-generated method stub
	Solution solver = new Solution();
	int quotient = solver.divide(5000, 14);
	System.out.println(quotient);
    }

    private static class Solution {
	public int divide(int dividend, int divisor) {
	    // Integer.MIN_VALUE / -1 is the only edge case that we need to worry about
	    // this will make result to be 2^31 which overflows the Integer.MAX_VALUE
	    // 1 << 31 is equal to Integer.MIN_VALUE
	    if (dividend == 1 << 31 && divisor == -1) {
		// Integer.MAX_VALUE
		return (1 << 31) - 1;
	    } else {
		int absDividend = Math.abs(dividend);
		int absDivisor = Math.abs(divisor);
		int quotient = 0;
		int x = 0;

		while (absDividend - absDivisor >= 0) {
		    x = 0;
		    while (absDividend - (absDivisor << x << 1) >= 0) {
			x++;
		    }
		    quotient += 1 << x;
		    absDividend -= absDivisor << x;
		}
		return (dividend > 0) == (divisor > 0) ? quotient : -quotient;
	    }
	}
    }

}
