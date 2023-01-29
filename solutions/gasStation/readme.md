# Gas Station problem
<img width="842" alt="image" src="https://user-images.githubusercontent.com/25105806/165003349-5d06c733-d1a2-4fba-8a02-fac9699b81ab.png">
<img width="850" alt="image" src="https://user-images.githubusercontent.com/25105806/165003360-10fc1fc1-95cd-466a-947b-aa2966635922.png">


Leetcode link: https://leetcode.com/problems/gas-station/

<br/>

### Approach 1: Brute Force, canCompleteCircuitBruteForce()
This solution leads to TLE.

The idea is simply to try each gas station, see if them can complete a circuit. Thus uses nested loop.

```cpp
int canCompleteCircuitBruteForce(vector<int>& gas, vector<int>& cost) {
    int n = gas.size();
    int result = -1;
    // try all possible starting index
    for (int start = 0; start < n; start++) {
        int tank = 0;
        // we have to iterate n times to complete circuit
        for (int i = start; i < n + start; i++) {
            if (tank < 0) {
                break;
            } else {
                tank += gas.at(i % n);
                tank -= cost.at(i % n);
            }
        }
        if (tank >= 0) {
            result = start;
            break;
        }
    }
    return result;
}
```

Time complexity is O(n^2)

<br/>

### Approach 2: Greedy, canCompleteCircuitGreedy()
Credits to: https://www.youtube.com/watch?v=lJwbPZGo05A

From the question statement we can see that if the sum of gas is smaller than the sum of cost, then there is no solution. If the sum of gas is greater than the sum of cost, there must be a solution and it's unique.

The idea is to go through the `gas` list only once, calculate the current volume in the tank as we go from one station to the next. If at some stations, the `tank` value dips below 0, which means we cannot go any further and we have not yet completed a circuit, then this means the current start position is not a valid solution. We should update the `start` position to be `i+1` where `i` is the traversal index. 

Our task is to find the starting index where the remaining (to the end of list) sum of cost is smaller than the sum of gas, which means we can complete a circuit, because there must be one unique solution and at any point the tank volume cannot dip below 0. 

```CPP
int canCompleteCircuitGreedy(vector<int>& gas, vector<int>& cost) {
    int gasSum = accumulate(gas.begin(), gas.end(), 0);
    int costSum = accumulate(cost.begin(), cost.end(), 0);
    if (gasSum < costSum) {
        // make sure sum of gas is greater than sum of cost
        // otherwise we must not complete
        return -1;
    } else {
        // it is guaranteed that there is an unique solution
        int result = 0;
        int tank = 0;
        // we only need to go through the list once because we only need to
        // find the starting index of gas that will not make the sum of tank dips below 0
        // since we made sure that gasSum >= costSum, the remaining sum must be smaller than current tank
        // which means we can complete a circuit
        for (int i = 0; i < gas.size(); i++) {
            tank += (gas.at(i) - cost.at(i));
            if (tank < 0) {
                // current result is not valid, we should update the result
                result = i + 1;
                tank = 0;
            }
        }
        return result;
    }
}
```

Time complexity is O(n):\
<img width="628" alt="image" src="https://user-images.githubusercontent.com/25105806/165004070-e11d1a08-c161-4099-85b4-ed12ee45a0a8.png">

<br />

### Approach 3: Greedy, canCompleteCircuitGreedy2()
This solution has identical idea as approach 2 but uses different implementation: `totalSurplus` is used to see if sum of gas is greater than sum of cost, turns out we don't need to calculate this separately, but calculate it in the loop. The logic of `totalSurplus` is independent from the remaining of the code in the loop.

```cpp
int canCompleteCircuitGreedy2(vector<int>& gas, vector<int>& cost) {
    int result = 0;
    int tank = 0;
    // totalSurplus is used to see if sum of gas is greater than sum of cost
    // turns out we don't need to calculate this separately, but in the loop
    int totalSurplus = 0;
    for (int i = 0; i < gas.size(); i++) {
        tank += (gas.at(i) - cost.at(i));
        totalSurplus += (gas.at(i) - cost.at(i));
        if (tank < 0) {
            // current result is not valid, we should update the result
            result = i + 1;
            tank = 0;
        }
    }
    return totalSurplus < 0 ? -1 : result;
}
```


Time complexity is O(n):\
<img width="626" alt="image" src="https://user-images.githubusercontent.com/25105806/165004276-ad6fd6f4-1773-433b-b9e2-6a0af48b1c67.png">

