# Reverse Integer problem
* Given a signed 32-bit integer `x`, return `x` with its digits reversed. If reversing `x` causes the value to go outside the signed 32-bit integer range `[-2^31, 2^31 - 1]`, then return `0`.

### Approach 1: Math, reverse()
Simply pop up the least number(tail) each time, add it to the result by `tmp = tmp * 10 + tail`, note that we need to check overflow indirectly because if the overflow happened, `tmp` will not be original value anymore, hence I test whether `tmp / 10 == rev`.
![image](https://user-images.githubusercontent.com/25105806/118201698-e769a600-b40c-11eb-80d3-8f30d932fd7e.png)
