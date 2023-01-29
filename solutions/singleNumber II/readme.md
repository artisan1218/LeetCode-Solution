# Single Number II problem
![image](https://user-images.githubusercontent.com/25105806/168681257-61b8b42a-0118-4419-844c-e1aba2e357c3.png)

Leetcode link: https://leetcode.com/problems/single-number-ii/

<br />


### Approach 1: Count Bits, singleNumberCountBit()
Credits to: https://www.youtube.com/watch?v=cOFAmaMBVps

Since we are guaranteed to have all numbers appeared exact 3 times except for one number, and we know that each number is represented internally by a 32-bit number of 0/1, we can then count the total number of 1's at each position, get the mod by 3 and convert the remaining number back to integer to get the answer.

The idea is that every number that appears 3 times will have a sum of bit at each position the multiple of 3. We can then take mod of 3 on that sum to get rid of them. The only remaining number will be the answer.

<img src="https://user-images.githubusercontent.com/25105806/168684491-579d8ea5-3d65-413f-b295-21b961db47b5.jpg" width=50%, height=50%>

code:
```cpp
int singleNumberCountBit(vector<int>& nums) {
    int result = 0;
    for (int b = 0; b < 32; b++) {
        int sum = 0;
        for (const auto& num : nums) {
            // to see if the bth position of the 32bit int num is a 1
            // & 1 is to check if the bit is set to 1
            // we can actually skip the == 1 part, as number 1 or 0 can be used as boolean
            if (1 == ((num >> b) & 1)) {
                sum++;
            }
        }
        sum %= 3;

        if (sum != 0) {
            result += sum << b;
        }
    }
    return result;
}
```

The logic here `(num >> b) & 1` is to see whether the bit at position `b` of `num` is a 1

Time complexity is O(32n), which is O(n) and space complexity is O(1):\
![image](https://user-images.githubusercontent.com/25105806/168684932-da1ed4f0-ea79-4ccf-834f-bb5d0a672a98.png)

<br />

### Approach 2: Construct new logic operation, singleNumberLogic()

This solution is the optimal solution and not easy to understand. Credits to: 
1. https://leetcode.cn/problems/single-number-ii/solution/gong-shui-san-xie-yi-ti-san-jie-ha-xi-bi-fku8/
2. https://leetcode.cn/problems/single-number-ii/solution/luo-ji-dian-lu-jiao-du-xiang-xi-fen-xi-gai-ti-si-l/
3. https://leetcode.cn/problems/single-number-ii/solution/zhi-chu-xian-yi-ci-de-shu-zi-ii-by-leetc-23t6/



The idea is to think of a new logic operator such that:
1. n \* n \* n = 0
2. n \* 0 = n

where `*` is the new operator and `n` is the number.

We want to make sure that the number that appears 3 times will be calculated back to 0 and the number that appears once will stay at its original value. 


Therefore, we can build a truth table based on the above logic:\
<img src="https://user-images.githubusercontent.com/25105806/168687148-39a85127-02b9-4d90-a72f-55ab6e3fad17.jpg" width="50%" height="50%">

where `x` and `y` denotes the current state. Since we have to store 3 states, we need to use at least two variables. 
1. `00` denotes the state of seen 3 times of a number, or initial state
2. `01` denotes the state of seen 1 times of a number
3. `10` denotes the state of seen 2 times of a number

`z` is the new number `num`, `x'` and `y'` is the new `x` and `y`.


We can derive the following rule based on the truth table:\
<img src="https://user-images.githubusercontent.com/25105806/168687745-e3ca215a-3025-41b7-9417-74eb7ea956b1.jpg" width="30%" height="30%">

Note that `x'` can be written as the following format, which is simpler:\
<img src="https://user-images.githubusercontent.com/25105806/168688652-5aefcebe-8fb1-458f-bf1f-13bbbd8eb575.jpg" width="30%" height="30%">


Next step is simply calculate all number in `nums` using the derived rule, `a` is `x` and `b` is `y`:

Note that the result will be stored in `b` because if `a` and `b` are all 0 and we performan the operator on the new number, `y`(`b`) will hold a 1, which will be the answer.

Full code:
```cpp
int singleNumberLogic(vector<int>& nums) {
    int a = 0, b = 0;
    for (int num : nums) {
        b = ~a & (b ^ num);
        a = ~b & (a ^ num);
    }
    return b;
}
```

Time complexity is O(n) and space complexity is O(1):\
![image](https://user-images.githubusercontent.com/25105806/168689115-b8e531cc-ec97-4239-b677-8463e2b59902.png)
