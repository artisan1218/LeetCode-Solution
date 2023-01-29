#include <iostream>
#include <numeric> // std::accumulate
#include <vector>

using namespace std;

class Solution {
public:
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
};

main() {
    Solution solver;
    vector<int> ratings = {1, 0, 2};
    cout << solver.candyOnePass(ratings) << endl;
    return 0;
}
