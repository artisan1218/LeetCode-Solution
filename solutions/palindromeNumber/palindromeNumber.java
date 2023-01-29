
public class palindromeNumber {

    public static void main(String[] args) {
	// TODO Auto-generated method stub
	int x = 1234;
	System.out.println(isPalindrome(x));
    }

    public static boolean isPalindrome(int x) {
	int reverse = 0;
	int ori = x;
	if (x < 0) {
	    return false;
	} else {
	    while (x > 0) {
		reverse = reverse * 10 + x % 10;
		x = x / 10;
	    }
	}
	return reverse == ori;
    }

}
