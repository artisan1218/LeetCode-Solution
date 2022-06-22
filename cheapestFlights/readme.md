# Cheapest Flights Within K Stops problem
![image](https://user-images.githubusercontent.com/25105806/174955209-6ce712d2-6444-46fe-bf82-c865920c3ac2.png)


Leetcode link: https://leetcode.com/problems/cheapest-flights-within-k-stops/

<br />

### Approach 1: Dijkstra's Algorithm, findCheapestPriceDijkstra()

Reference: https://www.youtube.com/watch?v=vWgoPTvQ3Rw

Since we're looking for the cheapest price of a path from `src` to `dst`, it is easy to think of Dijkstra's algorithm. However, we cannot directly use this algorithm because there is a limition on the number of nodes that we can use, which is `k` stops. To adopt this problem, there are several changes in the modified Dijkstra's algorithm:
1. We add another variable `availableSteps` to mark the remaining number of stops we can make at current city allowed by `k`. If this number is below 0, we should not keep exploring its neighbors because there is no way to get from `src` to this city within `k` stops.
2. In traditional Dijkstra's algorithm, each node can only be visited once and this is done by maintaining a hashset `visited` where we avoid adding seen nodes to the min-heap. However, with the new condition `k` stops, it is possible that we visit certain city for more than once because some paths will get to a city with less stops, which we will need to consider again. 

Therefore, we maintain a list called `maxSteps` which stores the max number of available steps at each city and control 'adding neighboring cities' to min-heap by comparing current available steps with the max steps in `maxSteps`, rather than a simple 'visited' hashset.

The is similar to loop through all `k` stops with a standard Dijkstra's algorithm.

```cpp
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
```

Actual running time:
![image](https://user-images.githubusercontent.com/25105806/174957668-63bef252-fa3b-4c7c-acff-59093655d5f5.png)


<br />

### Approach 2: Bellman Ford's Algorithm, findCheapestPriceBellmanFord()

Credits to: https://www.youtube.com/watch?v=5eIK3zUdYmE

Bellman Ford's algorithm is a perfect choice at this problem. The algorithm is easy to understand: we will loop through `k`, starting at `k=0`. Maintaining two lists that store the the cost it takes to get from `src` to each city. At each iteration, we will go over the `flights` list, calculate the cumulative cost to get to each city and update the list. However, there are somethings to notice:

We have two lists, and the two lists are the same at the begining of each iteration. When update the cumulative cost to each city, we will only update on the second list, which is called `tmpPrices`. But we will compare the recorded price at each city in the first list `price`. This way we can keep track of the number of stops, because if we use the same list to compare and update, we may compare a value that we've just updated, which means we just take one more stop to get to current city, which will be wrong. So we only copy the value of `tmpPrices` to `prices` upon finishing the price update at each iteration.



```cpp
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
```

Time complexity is O(k\*n):
![image](https://user-images.githubusercontent.com/25105806/174959185-9e31ce09-e1ac-4521-914e-4c542a790e92.png)

<br />

### Approach 3: Dynamic Programming, findCheapestPriceDP()

Reference: https://leetcode.cn/problems/cheapest-flights-within-k-stops/solution/k-zhan-zhong-zhuan-nei-zui-bian-yi-de-ha-abzi/

The idea is pretty similar to approach #2, but we use a 2d vector (a table) to store the prices. The table `dp[2][3]=4` means the price of getting from `src` to city 3 within 2 stops is 4.

The state transition function can be defined as `dp[stops][to] = min(dp[stops][to], dp[stops - 1][from] + cost);`. We simply compare the current price of getting to a city with the price of getting to previous city plus the cost from previous city to current city. There may be multiple routes we can use to reach a city, so we need to use a `min()` function to compare.

Notice that we always compare the price of a city with previous row, which is `stops - 1`. This is the same as `tmpPrices` in approach #2, we have to avoid comparing and updating the same row.

```cpp
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
```

Time complexity is O(k\*n):
![image](https://user-images.githubusercontent.com/25105806/174961797-2737c542-227c-49a8-8adf-15e3c86cbe90.png)
