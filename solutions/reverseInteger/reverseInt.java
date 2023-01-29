
public class reverseInt {
    public static void main(String[] args) {
	System.out.println(reverse(1534236469));
    }

    public static int reverse(int x) {
	int rev = 0;
	int tmp = 0;
	while (x != 0) {
	    int tail = x % 10;
	    x = x / 10;
	    tmp = tmp * 10 + tail;
	    // test if tmp exceeds the integer limit, we cannot simply compare it with
	    // Integer.MAX_VALUE because if the overflow happened, tmp will not be original
	    // value
	    if (tmp / 10 != rev) {
		return 0;
	    } else {
		rev = tmp;
	    }
	}
	return rev;
    }
}
