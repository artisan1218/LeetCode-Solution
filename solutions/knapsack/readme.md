# 0/1 Knapsack problem
Given a list of items with different value and different weight, a backpack and a weight limit, find the combination of items to be included in the backpack that maximize the value without exceeding the weight limit. The 0/1 means we can only choose to include or exclude the item, cannot break the item or use certian item for mulitple times.

Reference link: 
1. https://www.youtube.com/watch?v=uQj5UNhCPuo&list=PLPF7kEFdTM01pt_t39BC5nWdju4eskICf
2. https://www.youtube.com/watch?v=xCbYmUPvc2Q&list=PLPF7kEFdTM01pt_t39BC5nWdju4eskICf
3. https://www.youtube.com/watch?v=8LusJS5-AGo&list=PLPF7kEFdTM01pt_t39BC5nWdju4eskICf

<br/>

### Approach 1: Genetic Algorithm, evolution(), Python
The genetic algorithm is used to solve the complex problem in a quick but non-deterministic way. Non-deterministic means we are not guaranteed to get the optimal solution everytime we run the algorithm, however, the sub-optimal solution is also good enough and quick to get. 

The genetic algorithm simulates the meiosis process of the cell. The structure of the problem is:
1. Model the problem solution in terms of an array of numbers, this is used to represent the genome. In this problem, the genome is a list of 0 or 1 whereas 0 means the absence of an item in the knapsack and 1 means the presence of an item in the knapsack. The index of 0 or 1 is the index of the item.
2. Fina a proper way to measure the fitness of a genome. This answers the question 'how well does the current genome perform?' and we need to rank the genomes by their fitness score. In this problem, the fitness of a genome is defined as the total value of that combination. Clearly, the higher the value is, the better. But if the total weight of the combination exceeds the weight limit of the knapsack, the value will be reset to 0 because we cannot carray that many items.
3. Figure out the `crossover` and `mutation` function. Crossover represent the crossover process of two genome, in this problem, the crossover means exchange the upper/lower part of the genome between two parents. Mutation represent the random mutation that may happen to a genome. 

    For example if the two best performing parents are `10101111` and `11010010`, then their offsprings will be `10100010` and `11011111`. We simply exchange part of the parent with another parent. This step is very important because the crossover process will introduce the possibilty of generating better performing offspring. Just like two good parents will likely to have an even better child. However, it is also possible to generate a worse child, but we can overcome this by having lots of parents, then we will have a higher odds of finding the better offsprings.

    The mutation will happen randomly after the crossover. For example the last number at `10100010` may mutate to 1, resulting `10100011` genome.

Next all we need to do is to setup the population and let the evolution begin:
```python3
def evolution(populationSize, generationLimit, items, fitnessFunc):
    population = generatePopulation(populationSize, lengthOfGenome=len(items)) # random initialization

    for i in range(generationLimit):
        bestIndividual = sorted(population, key=lambda genome: fitnessFunc(genome), reverse=True)[0]
        # the individual already has good enough performance
        if fitnessFunc(bestIndividual) >= fitnessLimit:
            return bestIndividual, i
        else:
            next_gen = []
            for j in range(int(len(population)/2)):
                parents = selection(population, fitnessFunc)
                offspring1, offspring2 = crossover(parents[0], parents[1])
                offspring1 = mutation(offspring1)
                offspring2 = mutation(offspring2)
                next_gen.append(offspring1)
                next_gen.append(offspring2)
            population = next_gen

    return 'Result not found', -1
```

<br/>

### Approach 2: Dynamic Programming, knapsack(), C++
This solution is just the traditional way of solving such problem. We will use a 2d vector as dp table. The columns represent the weight limit of the knapsack starting from 0 to weight limit. The rows represent the items. Each spot of the dp table means the maximum value we can get from `items[0:i]` and weight limit `j`. For example, `dp[3][6] = 5` means the max value we can get by taking items from the first four items and a knapsack with weight limit 6 is 5 dollars.

We will fill in the dp table row and row from left to right. At each spot, we answer the question: 'for current weight limit, can the knapsack holds this item?' and there are two options:
1. If the knapsack cannot hold the item, then the max value we can get has nothing to do with current item, which is the same as before, which is simply the value above this spot: `dp[i-1][j]`
2. If the knapsack can hold the item, then the max value is the value of current item, plus the value we can get by using the remaining weight limit. For example, if the weight limit is 6 and current item has a weight of 4 and value of 2, then we also have a spare weight limit of 6-4=2 to hold other items, and the value of this weight limit can be found in previoud dp row. So `value[i] + dp[i - 1][curCap - weight[i]]`

The bottom right spot of the dp table will be the max value we can get.

<br />

To know exacly which items we should include, we can traceback the dp table at the bottim right spot.
1. If the current value is the same as the value above it, then this means the value is not from 'including the current item', which means we should not include current item.
2. If the current value is not the same as the value above it, then this means the value if from 'including the current item', which means we should include the current item. Then we need to subtract the current item weight from weight limit, and keep looking for what items made up the remaining weight

Full code:
```cpp
vector<int> knapsack(vector<int> weight, vector<int> value, int limit) {
    vector<vector<int>> dp(weight.size(), vector<int>(limit + 1, 0));
    for (int cap = 0; cap < limit + 1; cap++) {
        if (cap >= weight[0]) {
            dp[0][cap] = value[0];
        }
    }

    // perform dp, calculating the weights
    for (int i = 1; i < dp.size(); i++) {
        for (int curCap = 0; curCap < dp.at(i).size(); curCap++) {
            if (curCap < weight.at(i)) {
                dp[i][curCap] = dp[i - 1][curCap];
            } else {
                dp[i][curCap] = max(value[i] + dp[i - 1][curCap - weight[i]], dp[i - 1][curCap]);
            }
        }
    }

    // reconstruct the items based on dp
    vector<int> result;
    int i = weight.size() - 1;
    int curWt = limit;
    while (curWt != 0) {
        if (i == 0 || dp[i][curWt] != dp[i - 1][curWt]) {
            result.push_back(i);
            curWt -= weight[i];
        }
        i--;
    }

    return result;
}
```

Time complexity is O(mn) and space complexity is also O(mn), m is the weight limit and n is the number of items.
