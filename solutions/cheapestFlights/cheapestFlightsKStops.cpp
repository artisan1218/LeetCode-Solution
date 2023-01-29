#include <iostream>
#include <queue>
#include <unordered_map>
#include <unordered_set>
#include <vector>

using namespace std;

class Solution {
public:
    // reference: https://www.youtube.com/watch?v=vWgoPTvQ3Rw
    int findCheapestPriceDijkstra(int n, vector<vector<int>>& flights, int src, int dst, int k) {
        // adjacency map of the flights graph
        unordered_map<int, vector<vector<int>>> adj;
        for (const auto f : flights) {
            if (adj.find(f.at(0)) == adj.end()) {
                adj[f.at(0)] = {{f.at(1), f.at(2)}};
            } else {
                adj[f.at(0)].push_back({f.at(1), f.at(2)});
            }
        }
        // src has no outgoing edges
        if (adj.find(src) == adj.end()) {
            return -1;
        }

        // initialize distances to all nodes as infinity
        unordered_map<int, int> dist;
        for (const auto f : flights) {
            if (dist.find(f.at(1)) == dist.end()) {
                dist[f.at(1)] = INT_MAX;
            }
        }
        // dst has not inbound edges
        if (dist.find(dst) == dist.end()) {
            return -1;
        }

        // maxSteps holds the maximum available remaining steps we can take at each city
        unordered_map<int, int> maxSteps;
        for (auto f : flights) {
            if (maxSteps.find(f.at(0)) == maxSteps.end()) {
                maxSteps[f.at(0)] = INT_MIN;
            }
            if (maxSteps.find(f.at(1)) == maxSteps.end()) {
                maxSteps[f.at(1)] = INT_MIN;
            }
        }

        struct comparator {
            bool operator()(const vector<int>& a, vector<int>& b) {
                return a.at(2) > b.at(2);
            }
        };
        priority_queue<vector<int>, vector<vector<int>>, comparator> minHeap;
        minHeap.push({src, k + 1, 0});

        while (minHeap.size() != 0) {
            auto record = minHeap.top();
            int curCity = record[0];
            int availableSteps = record[1];
            int cost = record[2];
            minHeap.pop();

            if (availableSteps >= 0) { // this is a valid move
                // update the max available steps we have at curCity
                if (availableSteps > maxSteps[curCity]) {
                    maxSteps[curCity] = availableSteps;
                }

                // update the minimum distance
                if (cost < dist[curCity]) {
                    dist[curCity] = cost;
                }

                // BFS, explore all connected neighbor cities
                for (const auto& nei : adj[curCity]) {
                    // allow revisiting the same node if we have availableSteps greater than current record
                    if (availableSteps - 1 > maxSteps[nei[0]]) {
                        minHeap.push({nei[0], availableSteps - 1, cost + nei[1]});
                    }
                }
            }
        }

        return dist[dst] == INT_MAX ? -1 : dist[dst];
    }

    // credits: https://www.youtube.com/watch?v=5eIK3zUdYmE
    int findCheapestPriceBellmanFord(int n, vector<vector<int>>& flights, int src, int dst, int k) {
        vector<int> prices(n, INT_MAX);
        prices.at(src) = 0;

        vector<int> tmpPrices = prices;
        for (int i = 0; i < k + 1; i++) {
            tmpPrices = prices;
            for (const auto& f : flights) {
                int src = f[0];
                int dst = f[1];
                int p = f[2];
                if (prices[src] == INT_MAX) {
                    continue; // we haven't reached this node, we don't know the cost to reach src yet
                }
                // we've found a new low cost to reach dst
                // but don't update the prices vector yet, instead updating tmpPrices
                // because we may end up comparing a value that we've just updated in previous iteration
                // this will make sure we don't use more stops than k
                // prices is used to keep track of the min cost of path with exact i stops
                // so we cannot update the prices until we've finished iterating all flights
                if (p + prices[src] < tmpPrices[dst]) {
                    tmpPrices[dst] = p + prices[src];
                }
            }
            prices = tmpPrices;
        }

        return prices[dst] == INT_MAX ? -1 : prices[dst];
    }

    // reference: https://leetcode.cn/problems/cheapest-flights-within-k-stops/solution/k-zhan-zhong-zhuan-nei-zui-bian-yi-de-ha-abzi/
    int findCheapestPriceDP(int n, vector<vector<int>>& flights, int src, int dst, int k) {
        vector<vector<int>> dp(k + 1, vector<int>(n, 1e5 + 1));
        dp[0][src] = 0; // the cost to get src within 0 stop is 0

        // initialize the base case where it takes 0 stops to get from src to a city
        for (const auto& f : flights) {
            if (f[0] == src) {
                dp[0][f[1]] = f[2];
            }
        }

        // dp starts
        for (int stops = 1; stops < dp.size(); stops++) {
            dp[stops][src] = 0; // to get to src city, cost is always 0 regardless of the stops
            for (const auto& f : flights) {
                int from = f[0];
                int to = f[1];
                int cost = f[2];
                // dp[stops-1][from] + cost is the cost to get from previous city to current city
                dp[stops][to] = min(dp[stops][to], dp[stops - 1][from] + cost);
            }
        }
        return dp[k][dst] == 1e5 + 1 ? -1 : dp[k][dst];
    }
};

int main() {
    Solution solver;
    int n = 4;
    vector<vector<int>> flights = {{0, 1, 100}, {1, 2, 100}, {2, 0, 100}, {1, 3, 600}, {2, 3, 200}};
    int src = 0;
    int dst = 3;
    int k = 1;
    int price = solver.findCheapestPriceDP(n, flights, src, dst, k);
    cout << price << '\n';
    return 0;
}