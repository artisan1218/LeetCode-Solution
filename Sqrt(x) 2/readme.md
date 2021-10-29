# Sqrt(x) problem
* Given a non-negative integer `x`, compute and return the square root of `x`.
* Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.
* Note: You are not allowed to use any built-in exponent function or operator, such as `pow(x, 0.5)` or `x ** 0.5`.

### Approach 1: Bruth Force, mySqrtIncrementOne()
This approach simply will test all possible answers from 1 and increment 1 each time until we find the correct square root. 

Time complexity is O(sqrt(n)) because we will loop for sqrt(n) times to find the correct root:\
![dc98fa160c123617e32bf4db53a0d94](https://user-images.githubusercontent.com/25105806/130344946-8cc1dc1d-0acc-4af0-ad1e-25d053895b91.png)

<br />

### Approach 2: Binary Search, mySqrtBinarySearch()
This is similar to approach 1 but we first use binary search to narrow down the range for the possible answers by doubling the answer each time in the loop. Then use same strategy as approach 1 to find the correct square root by testing all numbers in the range. This will save us some time when the correct answer is large because doubling will use log() time.

Actual running time, we can see that the running time is indeed a lot faster:\
![c47758c2e02c041c6919ed00bfbf774](https://user-images.githubusercontent.com/25105806/130345057-2b33fdd7-d663-4301-b08b-8f864139b62c.png)


<br />

### Approach 3: Newton's method, mySqrtNewton()
This approach is based on Newton's method to approximate square root. The formula is shown below:\
![image](https://user-images.githubusercontent.com/25105806/130345122-7d86394a-e727-4f5e-84b3-2bba130f688f.png)


Actual running time is the fastest among all three approaches:\
![image](https://user-images.githubusercontent.com/25105806/130345134-9d1bb0f1-57c4-4dbf-9b2e-1674bc1c9328.png)

