# Roman to Integer problem
* Roman numerals are represented by seven different symbols: `I`, `V`, `X`, `L`, `C`, `D` and `M`.
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
Given a roman numeral, convert it to an integer.

Leetcode link: https://leetcode.com/problems/roman-to-integer/

<br />

### Approach 1: Math, romanToInt()
Simply iterate through the given String `s`, convert the single character to corresponding integer value and compare it with its immediate preceeding value. 
1. If the current value is smaller than the preceedingt value, then we're good by simply adding the value to `result`
2. If the current value is greater than the preceeding value, e.g. `IV`, 4 is smaller than 1, we need to do a little math here by adding `digit - 2 * preceedingDigit`, which is `4-2*1=2` in this case. So the final value will be `1+2=3`.

```java
public static int romanToInt(String s) {
    Map < Character, Integer > map = new HashMap < > ();
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
```

Time complexity is O(n) since we iterate over each char of the given string `s`.
![image](https://user-images.githubusercontent.com/25105806/118631228-23da3080-b784-11eb-9a7f-93ff46d97a44.png)

