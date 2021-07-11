# Pow(x, n) problem
* Implement `pow(x, n)`, which calculates `x` raised to the power `n` (i.e., x^n).


### Approach 1: Math, myPow()

2^3 can be written as `2*2*2`. If we simply use a loop to do the multiplication, the running time will be very long and lead to TLE. Instead, it can be written as `2*4`, where 4 is equal to `2*2` and we only loop twice. More specifically, every time we multiply the result, we also multiply `x` by itself and halve the `n`.

So 3^5 can be written as `3*81` because:

```
x = 3
n = 5

n%2==1, result = 3, x=3*3=9, n=n//2=2
n%2==0, result = 3, x=9*9=81, n=n//2=1
n%2==0, result = 3*81, n=n//2=0, break

return result=243
```

Time complexity is O(logn), actual running time:

![image](https://user-images.githubusercontent.com/25105806/125179669-3df12780-e1a5-11eb-8976-141d1be7002a.png)


