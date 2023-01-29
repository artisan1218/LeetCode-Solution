# Single Number problem
![1652230762(1)](https://user-images.githubusercontent.com/25105806/167748172-562973f4-16c5-4c11-9e7f-f5c7c02c3be1.png)

Leetcode link: https://leetcode.com/problems/single-number/

<br />


### Approach 1: Count, singleNumberCount()
The idea is to use a map to count the occurrence of each number in `nums` in linear time and find the number that has only one count.

```cpp
int singleNumberCount(vector<int>& nums) {
    unordered_map<int, int> map;
    for (const auto& num : nums) {
        if (map.find(num) != map.end()) {
            map[num]++;
        } else {
            map[num] = 1;
        }
    }
    for (const auto& pair : map) {
        if (pair.second == 1) {
            return pair.first;
        }
    }
    return -1;
}
```

Time complexity is O(n) and space complexity is O(n):\
![image](https://user-images.githubusercontent.com/25105806/167748478-0af7d429-9ef4-4041-8cc8-7b96f88f16e9.png)

<br />

### Approach 2: Sort, singleNumberSort()
The idea is to first sort the `nums` array, so that same number will appear right next to each other. We then simply compare the numbers pair by pair and return the single one.

```cpp
int singleNumberSort(vector<int>& nums) {
    sort(nums.begin(), nums.end());
    for (int i = 1; i < nums.size(); i = i + 2) {
        if (nums.at(i) != nums.at(i - 1)) {
            return nums.at(i - 1);
        }
    }
    return nums.at(nums.size() - 1);
}
```

Time complexity is O(nlogn) because of the sorting, space complexity is O(1):\
![image](https://user-images.githubusercontent.com/25105806/167748676-d27c21af-a281-4c57-89d4-1ee19e00b73e.png)\

<br />

### Approach 3: Bitwise Manipulation, singleNumberBit()
Credits to: https://leetcode.com/problems/single-number/discuss/1771720/C%2B%2B-EASY-SOLUTIONS-(SORTING-XOR-MAPS-(OR-FREQUENCY-ARRAY))

The idea is based on the XOR operation:
1. A^A=0
2. A^B^A=B
3. (A^A^B) = (B^A^A) = (A^B^A) = B This shows that position doesn't matter.

We can simply go over the `nums` array once, performe the XOR operation on each of the element against the `result` with initial value of 0, the result will be the value of that single number.

```cpp
int singleNumberBit(vector<int>& nums) {
    int result = 0;
    for (const auto& num : nums) {
        result = result ^ num;
    }
    return result;
}
```

Time complexity is O(n) and space complexity is O(1). This is the optimal solution:\
![image](https://user-images.githubusercontent.com/25105806/167748938-61ac2abd-3b6f-4209-92fe-b3a2f7a3dbc7.png)

