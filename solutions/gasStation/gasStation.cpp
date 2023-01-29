#include <iostream>
#include <numeric>
#include <vector>
using namespace std;

class Solution {
public:
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

    // credits to: https://www.youtube.com/watch?v=lJwbPZGo05A
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
};

int main() {
    vector<int> gas = {2, 3, 4};
    vector<int> cost = {3, 4, 3};
    Solution solver;
    cout << solver.canCompleteCircuitGreedy(gas, cost) << endl;
}