# Integer to Roman problem
* Given an integer, convert it to a roman numeral. Roman numerals are represented by seven different symbols: `I`, `V`, `X`, `L`, `C`, `D` and `M`.
```
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
```

Leetcode link: https://leetcode.com/problems/integer-to-roman/

<br/>

### Approach 1: Naive, intToRomanLoop()
This approach is to go through the given `num` digit by digit and append the corresponding symbols to the `result`. The corresponding symbol of the given digit is determined by the value of the digit and the `fold`, which keepk track of multiple that we're currently dealing with, ranges from 1, 10, 100, 1000.
1. The fold is 1, then the symbols can only be `I`, `V`, `X`
2. The fold is 10, then the symbols can be `X`, `L`, `C`
3. The fold is 100, then the symbols can be `C`, `D`, `M`
4. The fold is 1000, then the symbols can be `M`


```java
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
```


Running time is fairly slow due to the String concatenations:\
![image](https://user-images.githubusercontent.com/25105806/118616818-e58a4480-b776-11eb-9a51-41573aa689b8.png)

<br/>

### Approach 2: Math, intToRomanMath()
Credits to https://leetcode.com/problems/integer-to-roman/discuss/6274/Simple-Solution

Since each multiple out of 1, 10, 100, 1000 can only have certain symbols, we can list them all and store them as arrays. Then use simple math to match each of the symbols. This method is probably the most elegant way of solving this probelm. 

```java
public static String intToRomanMath(int num) {
	String M[] = { "", "M", "MM", "MMM" };
	String C[] = { "", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM" };
	String X[] = { "", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC" };
	String I[] = { "", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX" };
	StringBuilder result = new StringBuilder("");
	result.append(M[num / 1000]).append(C[(num % 1000) / 100]).append(X[(num % 100) / 10]).append(I[num % 10]);
	return result.toString();
    }
```

Running time is better than approach 1 because we've avoided using String concatenations, logic is also much clear:\
![image](https://user-images.githubusercontent.com/25105806/118619003-0bb0e400-b779-11eb-976a-541ec8a3b0d6.png)

<br/>

### Approach 3: Math, intToRomanMath2()
Credits to https://leetcode.com/problems/integer-to-roman/discuss/6310/My-java-solution-easy-to-understand

Similar to approach 2, we can list symbols for each multiple out of 1, 10, 100, 1000, but this time we only list unique symbols but not all of them. For example `III` is just `I` repeating for 3 times and we can use a loop to denoting this. This way, we can save some uncessary spaces. 

```java
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
```

Running time is roughly the same, but memory usage is better:\
![image](https://user-images.githubusercontent.com/25105806/118618106-2171d980-b778-11eb-8dc2-4d1a9319e755.png)



