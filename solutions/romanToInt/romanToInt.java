import java.util.HashMap;
import java.util.Map;

public class romanToInt {

    public static void main(String[] args) {
	// TODO Auto-generated method stub
	System.out.println(romanToInt("XIV"));
    }

    public static int romanToInt(String s) {
	Map<Character, Integer> map = new HashMap<>();
	map.put('I', 1);
	map.put('V', 5);
	map.put('X', 10);
	map.put('L', 50);
	map.put('C', 100);
	map.put('D', 500);
	map.put('M', 1000);

	int result = 0;
	int prevDigit = 0;

	for (int i = 0; i < s.length(); i++) {
	    int digit = map.get(s.charAt(i));

	    if (digit <= prevDigit) {
		result = result + digit;
	    } else {
		result = result + (digit - 2 * prevDigit);
	    }
	    prevDigit = digit;
	}
	return result;
    }

}
