#include <cmath>
#include <iostream>
#include <set>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    string crackSafeBacktrack(int n, int k) {
        string result(n, '0');
        set<string> seen = {result};
        bakctrack(n, k, result, seen);
        return result;
    }

    bool bakctrack(int n, int k, string& cur, set<string>& seen) {
        if (seen.size() == pow(k, n)) {
            return true;
        }

        for (int i = 0; i < k; i++) {
            cur.append(to_string(i));                          // append the new char
            string password = cur.substr(cur.length() - n, n); // get the newly formed password
            if (seen.count(password) == 0) {
                // newly formed password is not seen before, we can add it to the set and append next one recursively
                seen.insert(password);
                if (bakctrack(n, k, cur, seen)) {
                    return true;
                }
                cur.pop_back();       // backtrack
                seen.erase(password); // backtrack
            } else {
                // the newly formed password is seen, we should try appending another char
                cur.pop_back();
            }
        }
        return false;
    }

    string crackSafeHierholzer(int n, int k) {
        int nodeNum = pow(k, n - 1);      // not pow(k, n) because each node represent the shared portion between passwords, which has length of n-1, so total number of nodes will be k^n-1 not k^n
        vector<int> side(nodeNum * k, 0); // each node has k out-degrees, so total of node*k edges
        string result;
        hierholzer(side, k, 0, result, nodeNum);
        result += string(n - 1, '0'); // append the starting string
        return result;
    }

    void hierholzer(vector<int>& side, int k, int edgeIdx, string& res, int nodeNum) {
        int currNode = edgeIdx % nodeNum;                           // convert edge index to node index
        for (int outboundIdx = 0; outboundIdx < k; outboundIdx++) { // iterate over all outdegree edges of each node
            int edgeIdx = currNode * k + outboundIdx;               // convert node idx and outdegree idx to edge idx
            if (side[edgeIdx] == 0) {                               // we haven't explored this edge yet
                side[edgeIdx]++;
                hierholzer(side, k, edgeIdx, res, nodeNum);
                res += to_string(outboundIdx);
            }
        }
    }
};

int main() {
    Solution solver;
    int n = 2;
    int k = 2;
    string result = solver.crackSafeHierholzer(n, k);
    cout << result << endl;

    return 0;
}