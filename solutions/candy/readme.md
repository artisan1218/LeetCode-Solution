# Candy problem
![image](https://user-images.githubusercontent.com/25105806/166880480-835f157b-d644-44f8-b667-4be257c38aa1.png)

Leetcode link: https://leetcode.com/problems/candy/

<br />

### Approach 1: Scan Twice from Both Direction, candyTwoPass()
The idea is to scan the `ratings` list twice, once from left to right and once from right to left. We use a single list `distribution` to store the candies.

When scanning from left, we only care about the case where current rating is higher than previous rating. In this case, we only need to make sure current child gets one more candy than previous child (the one on the left side of this child). We will worry about the case where current child has lower rating than previous child in the opposite direction scan. When scanning from right, we only care about the case where current child has higher ratings than next child (next child here means the one on the right) and current child has currently less or equal candy than the rigth child. In this case, we need to assign one more candy to current child than the child on his right side. 

Then simply sum up the `distribution` list to get the answer.

```cpp
int candyTwoPass(vector<int>& ratings) {
    vector<int> distribution(ratings.size(), 1);

    // left to right
    for (int i = 1; i < ratings.size(); i++) {
        if (ratings.at(i) > ratings.at(i - 1)) {
            distribution.at(i) = distribution.at(i - 1) + 1;
        }
    }
    // right to left
    for (int i = ratings.size() - 2; i >= 0; i--) {
        if (ratings.at(i) > ratings.at(i + 1) && distribution.at(i) <= distribution.at(i + 1)) {
            distribution.at(i) = distribution.at(i + 1) + 1;
        }
    }

    return accumulate(distribution.begin(), distribution.end(), 0);
}
```

Time complexity is O(n) and space complexity is (n) because we use `distribution` list to store the candies:
![image](https://user-images.githubusercontent.com/25105806/166882052-849a0b44-c0d4-4251-b629-4f06a41f825c.png)

<br />

### Approach 2: Scan Once, candyOnePass()

Credits to: https://leetcode-cn.com/problems/candy/solution/fen-fa-tang-guo-by-leetcode-solution-f01p/

In this solution, we only need to scan once from left to right. 

We can see the `ratings` list as several increasing subarray and decreasing subarray. In the increasing subarray, we always assign one more candy to current child than previous child. This can be done by using a `pre` counter. When we are in a decreasing subarray, although technically we have to go back and increase the candy distribution to previous children, but since we only care about the number of candies, and this number can be represented by the length of descreasing subarray, we can simply add the length of decreasing subarray to result every time we see next child has lower rating.  

One special case we need to handle is when length of increasing subarray is equal to the length of decreasing subarray, we need to count the last child in previous increasing subarray into the decreasing subarray, which is to give one more candy to every child in the decreasing subarray.

```cpp
int candyOnePass(vector<int>& ratings) {
    int result = 1;
    int inc = 1; // length of increasing subarray
    int dec = 0; // length of decreasing subarray
    int pre = 1; // candy number of previous child

    for (int i = 1; i < ratings.size(); i++) {
        // current rating is greater than prev one, we're in an increasing subarray
        if (ratings.at(i) > ratings.at(i - 1)) {
            dec = 0; // no longer in decreasing subarray
            pre++;   // simply assign current child with one more candy
            result += pre;
            inc = pre; // pre is always the length of increasing subarray
        } else if (ratings.at(i) == ratings.at(i - 1)) {
            // current child has same rating as previous one
            // we only need to give 1 candy to this child
            inc = 1; // reset length of increasing subarray
            dec = 0;
            pre = 1;
            result += pre;
        } else {
            // we're in a decreasing subarray
            dec++;
            if (inc == dec) { // if two subarrays have same length, we need to give one more candy to the last child in previous increasing subarray
                dec++;        // simply increment dec by 1, as result+=dec will take account all number in the subarray in
            }
            result += dec; // give one more candy to everyone in the decreasing subarray, the increased total number of candies is equeal to the length of decreasing subarray
            pre = 1;       // reset pre to 1 as next increasing subarray will start from 1 candy
        }
    }
    return result;
}
```

Time complexity is O(n) and space complexity is O(1) as we only use fixed number of variables to keep track of the candies:
![image](https://user-images.githubusercontent.com/25105806/166883384-1df3efb5-1ea8-47d7-959e-eb41e990ed2c.png)

