# House Robber II problem
![image](https://user-images.githubusercontent.com/25105806/180586660-3ab53380-e9df-4eeb-a8b9-d86c3a7f46ee.png)


Leetcode link: https://leetcode.com/problems/house-robber-ii/

<br />

### Approach 1: Dynamic Programming, rob()
This solution is based on [House Robber I](https://github.com/artisan1218/LeetCode-Solution/tree/main/houseRobber). The only difference is that we have to consider the situation that the last house is connected with the first house. We don't need to modify the original dp solution, but simply run the solution twice with different starting and ending index of the `nums` array.

The first run is to include(rob) the first house but not including the last house: `nums[0:-1]`; The second run is to not include the first house and include the last house: `nums[1:]`.

We basically manually include two possible ways of starting robbery and let dp algorithm to solve the rest

![0356f6cdaceaaa791b899af061df2dd](https://user-images.githubusercontent.com/25105806/180586992-9f1818e4-a8d2-4f74-86a2-66847848eae0.jpg)


Full code:
```cpp
int rob(vector<int>& nums) {
    if (nums.size() == 1) {
        return nums[0];
    } else {
        // rob second one, then we can rob the last one
        // rob first one, then cannot rob the last one
        return max(helper(nums, 1, nums.size()), helper(nums, 0, nums.size() - 1));
    }
}

int helper(vector<int>& nums, int start, int end) {
    int pre = 0;
    int cur = 0;
    for (int i = start; i < end; i++) {
        int tmp = pre;
        pre = cur;
        cur = max(nums.at(i) + tmp, cur);
    }
    return cur;
}
```

Time complexity is O(n):\
![image](https://user-images.githubusercontent.com/25105806/180587034-8121cc66-482b-46a9-8bf2-1916823f5766.png)
