# Divide Two Integers problem
* Given two integers `dividend` and `divisor`, divide two integers without using multiplication, division, and mod operator.
* Return the quotient after dividing `dividend` by `divisor`.
* The integer division should truncate toward zero, which means losing its fractional part. For example, `truncate(8.345) = 8` and `truncate(-2.7335) = -2`.

Note: Assume we are dealing with an environment that could only store integers within the **32-bit** signed integer range: `[−2^31, 2^31 − 1]`. For this problem, assume that your function returns `2^31 − 1` **when the division result overflows**.

### Approach 1: Naive, Skipped()
The idea is very straightforward and comes from the definition of 'dividing': that is, how many `divisors` are contained in `dividend`. We simply subtract divisor from dividend once a time until `dividend` is smaller than `divisor`, which means `dividend` does not contain `divisor` anymore. \
For example: we divide 5000 by 14:
1. We first subtract 14 from 5000 for 256 times: 14\*256=3584 and 5000-3584=1416. Up to this step, quotient = 256
2. Then keep subtracting 14 from 1416, we can subtract 64 times: 14\*64=896, 1416-896=520. Up to this step, quotient = 256 + 64
3. Subtracting 14 from 520 for 32 times: 14\*32=448, 520-448=72. Up to this step, quotient = 256 + 64 + 32
4. Subtracting 14 from 72 for 4 times: 14\*4=56, 72-56=16. Up to this step, quotient = 256 + 64 + 32 + 4
5. Finally subtracting 14 from 16, 14\*1=16, 16-14=2 and 2<14. Finally, quotient = 256 + 64 + 32 + 4 + 1 = 357

The main downside of this approach is:
1. When the dividend(2^31-1) is large and divisor is small(1), the running time is slow because we simply subtract 1 from 2^31-1 2^31-1 times.
2. Hard to handle overflow issue

Time complexity is therefore O(n/m) where n is the value of `dividend` and m is the value of `divisor`.\
Note that this approach definitely works, but this will lead to ETL on leetcode.com

<br />

### Approach 2, Bit-wise Manipulation, divide()

Credits to:
1. https://leetcode.com/problems/divide-two-integers/discuss/142849/C%2B%2BJavaPython-Should-Not-Use-%22long%22-Int
2. https://leetcode.com/problems/divide-two-integers/discuss/13407/C%2B%2B-bit-manipulations
3. https://docs.oracle.com/javase/tutorial/java/nutsandbolts/op3.html

The idea of how bitwise manipulation works is similar to approach 1, but instead of subtract strictly `divisor` from `dividend` every time, we subtract `divisor * 2^x` from `dividend` where `x` is a multiplier that grows by 1 each time.

For example:
Suppose dividend = 15 and divisor = 3, 15 - 3 > 0.\
We now try to subtract more by shifting 3 to the left by 1 bit (6). Since 15 - 6 > 0, shift 6 again to 12. Now 15 - 12 > 0, shift 12 again to 24, which is larger than 15. \
So we can at most subtract 12 from 15. Since 12 is obtained by shifting 3 to left twice, it is 1 << 2 = 4 times of 3. We add 4 to an answer variable (initialized to be 0).\
The above process is like 15 = 3 * 4 + 3. We now get part of the quotient (4), with a remaining dividend 3.\
Then we repeat the above process by subtracting divisor = 3 from the remaining dividend = 3 and obtain 0. \
We are done. In this case, no shift happens. We simply add 1 << 0 = 1 to the answer variable.

-2^31 divide by -1 is the only edge case that we need to worry about. This will make result to be 2^31 which overflows the Integer.MAX_VALUE. We can simply return 2^31-1 when `dividend=-2^31` and `divisor=-1`.

Note that the in the code, the line ```absDivisor << x << 1``` can not be replaced with ```absDivisor << x + 1```. They may seem the same statement but will perform differently when overflow happens.
For example, in Java: ```1 << 31 << 1``` is `0` while ```1 << 32``` is `1`.

Time complexity is O(logN^2) because we will double the `divisor` every time we can subtract it from `dividend`, resulting in a much faster 'convergence'.

![image](https://user-images.githubusercontent.com/25105806/121135050-f6176300-c7e8-11eb-85dd-f8adb7130443.png)




