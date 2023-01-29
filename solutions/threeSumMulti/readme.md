# 3Sum With Multiplicity problem
![image](https://user-images.githubusercontent.com/25105806/179427879-afcfa37e-ac6d-4de4-9050-5003d3e25d56.png)


Leetcode link: https://leetcode.com/problems/3sum-with-multiplicity/

<br />

### Approach 1: Brute Force, threeSumMulti()

Credits to: https://leetcode.com/problems/3sum-with-multiplicity/discuss/181128/10-lines-Super-Super-Easy-Java-Solution

In this solution, we will use two pointers `i` and `j`, where `i` ranges from 0 to the end of `arr` and `j` ranges from 0 to `i`. We will count the occurrences of the twoSum `arr[i] + arr[j]` and then found the complement number `target - twoSum(i, j)` in the count and finally add it to the result.

We can do this in two nested loops by making `j` ranges from 0 to `i`, so that the calculated two sums are always before the `i` pointer, which means the result can be iteratively added

```cpp
int threeSumMulti(vector<int>& arr, int target) {
    int result = 0;
    unordered_map<int, int> map;
    int mod = 1e9 + 7;
    for (int i = 0; i < arr.size(); i++) {
        if (map.find(target - arr[i]) != map.end()) {
            result = (result + map[target - arr[i]]) % mod;
        }

        for (int j = 0; j < i; j++) {
            int twoSum = arr[i] + arr[j];
            if (map.find(twoSum) == map.end()) {
                map[twoSum] = 1;
            } else {
                map[twoSum]++;
            }
        }
    }
    return result;
}
```

Time complexity is O(n^2):\
![image](https://user-images.githubusercontent.com/25105806/179428749-4274841e-20c8-4b37-b87d-c96e03e94f87.png)

<br />

### Approach 2: Brute Force, threeSumMulti2()

Credits to: https://www.youtube.com/watch?v=jZcAldZP1ag

This solution is similar to approach #1 where we used nested two loops to count two sum and find the complement number. In this solution, instead of calculating two sum, we only calculate the occurrence of the 'complement' number and use nested two loops to form the two sum.


Note that `j` pointer ranges from `i+1` to the end of `arr` and we only count the orrurrence of numbers after current `i` pointer.

```cpp
int threeSumMulti2(vector<int>& arr, int target) {
    int mod = 1e9 + 7;
    int result = 0;
    for (int i = 0; i < arr.size(); i++) {
        vector<int> count(101, 0); // 0 <= arr[i] <= 100
        for (int j = i + 1; j < arr.size(); j++) {
            int k = target - arr[i] - arr[j];
            if (k >= 0 && k <= 100) {
                result = (result + count[k]) % mod;
            }
            count[arr[j]]++;
        }
    }
    return result;
}
```

Time complexity is O(n^2):\
![image](https://user-images.githubusercontent.com/25105806/179429017-53bd214b-be57-446c-9bde-742b091c9857.png)

<br />

### Approach 3: Math/Combination Formula, threeSumMultiMath()

Credits to: https://www.youtube.com/watch?v=jZcAldZP1ag

Instead of traditionally counting of each possible combination of `i`, `j` and `k`, we can also directly calculate the total number of combinations. 

We first need to use a loop to count the occurrence of each number in `arr`, then use nested two loop to iterate over all possible numbers in the arr, which ranges from 0 to 100, as stated in problem description. Same as before, calculate the complement number by `target - i - j`. We now have three variables `i`, `j` and `k` and there are three situations:
1. `i = j = k`: This can happen if the `arr` contains all same number. The total number of combinations is therefore `C n choose 3`, the formula is shown below:
    
    <img src="https://user-images.githubusercontent.com/25105806/179429365-6d768940-bd03-43ea-95dd-cbd34f998555.jpg" width="50%" height="50%">

2. `i = j and j != k`: This represent the case where only two of three numbers are the same. Then we need to calculate the product of the `count[k]` and `C n choose 2`, the formula is shown below:

    <img src="https://user-images.githubusercontent.com/25105806/179429466-770ddbdf-4b81-48e8-8b56-d1bb3afb321b.jpg" height="50%" width="50%">

    Note: case `i != j and j = k` is the same as `i = j and j != k` because they are in a loop
    
3. `i != j and j != k`: This represent the case where all three numbers are different, then we simply multiply the count of them together: `count[i] * count[j] * count[k]`.
    
    In actual code, we need to phrase it as `i < j && j < k` because this will remove duplicates counts




Full code:
```cpp
int threeSumMultiMath(vector<int>& arr, int target) {
    long count[101] = {0};
    for (auto num : arr) {
        count[num]++; // count the occurrence of each number
    }

    int mod = 1e9 + 7;
    long result = 0;
    for (int i = 0; i <= 100; i++) {
        for (int j = i; j <= 100; j++) {
            int k = target - i - j;
            if (k >= 0 && k <= 100) {
                if (i == j && j == k) {
                    // Combination: from count[i] choose 3
                    result += (count[i] * (count[i] - 1) * (count[i] - 2)) / 6;
                } else if (i == j && j != k) {
                    // Combination: from count[i] choose 2
                    result += (count[i] * (count[i] - 1) / 2) * count[k];
                } else if (i < j && j < k) {
                    result += (count[i] * count[j] * count[k]);
                } else {
                    continue;
                }
            }
        }
    }
    return result % mod;
}
```

Time complexity is O(n + 101\*101), O(n) is for the loop of counting occurrences and O(101\*101) is for the nested loop:
![image](https://user-images.githubusercontent.com/25105806/179429830-a95aabad-e89e-4c9d-9bdf-f45b0c74fed2.png)
