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

### Approach 1: Naive, intToRomanLoop()
This approach is to go through the given `num` digit by digit and append the corresponding symbols to the `result`. The corresponding symbol of the given digit is determined by the value of the digit and the `fold`, which keepk track of multiple that we're currently dealing with, ranges from 1, 10, 100, 1000.
1. The fold is 1, then the symbols can only be `I`, `V`, `X`
2. The fold is 10, then the symbols can be `X`, `L`, `C`
3. The fold is 100, then the symbols can be `C`, `D`, `M`
4. The fold is 1000, then the symbols can be `M`

Running time is fairly slow due to the String concatenations
![image](https://user-images.githubusercontent.com/25105806/118616818-e58a4480-b776-11eb-9a51-41573aa689b8.png)



### Approach 2: Math, intToRomanMath()
Credits to https://leetcode.com/problems/integer-to-roman/discuss/6274/Simple-Solution

Since each multiple out of 1, 10, 100, 1000 can only have certain symbols, we can list them all and store them as arrays. Then use simple math to match each of the symbols. This method is probably the most elegant way of solving this probelm. 

Running time is better than approach 1 because we've avoided using String concatenations, logic is also much clear.
![image](https://user-images.githubusercontent.com/25105806/118619003-0bb0e400-b779-11eb-976a-541ec8a3b0d6.png)



### Approach 3: Math, intToRomanMath2()
Credits to https://leetcode.com/problems/integer-to-roman/discuss/6310/My-java-solution-easy-to-understand

Similar to approach 2, we can list symbols for each multiple out of 1, 10, 100, 1000, but this time we only list unique symbols but not all of them. For example `III` is just `I` repeating for 3 times and we can use a loop to denoting this. This way, we can save some uncessary spaces. 

Running time is roughly the same, but memory usage is better.
![image](https://user-images.githubusercontent.com/25105806/118618106-2171d980-b778-11eb-8dc2-4d1a9319e755.png)



