#!/usr/bin/env python
# coding: utf-8

# In[1]:


from typing import List

class Solution:
    def mincostTicketsDFS(self, days: List[int], costs: List[int]) -> int:
        cache = dict()
        def dfs(i):
            if i>=len(days):
                return 0
            else:
                if i in cache:
                    return cache[i] # cache
                else:
                    minCost = float('inf')
                    # for each day, go over all three possible ways of purchasing tickets
                    # and choose the one with min cost
                    for day, cost in zip([1, 7, 30], costs):
                        # find the index of the next day that we need purchase ticket for
                        nextDayIdx = i
                        while nextDayIdx < len(days) and days[nextDayIdx] < days[i] + day:
                            nextDayIdx += 1
                        minCost = min(minCost, dfs(nextDayIdx) + cost)
                    cache[i] = minCost # cache    
                    return cache[i]
        
        return dfs(0)  
    
    def mincostTicketsDPFromBack(self, days: List[int], costs: List[int]) -> int:
        dp = dict()
        # scan from the back to beginning because today's choice depends on the future days
        for i in range(len(days)-1, -1, -1):
            dp[i] = float('inf')
            # for each day, go over all three possible ways of purchasing tickets
            # and choose the one with min cost
            for day, cost in zip([1, 7, 30], costs):
                # find the index of the next day that we need purchase ticket for
                nextDayIdx = i
                while nextDayIdx < len(days) and days[nextDayIdx] < days[i] + day:
                    nextDayIdx += 1
                dp[i] = min(dp[i], dp.get(nextDayIdx, 0) + cost)
                
        return dp[0] 
    
    def mincostTicketsDPFromStart(self, days: List[int], costs: List[int]) -> int:
        # DP Table, record for minimum cost of ticket to travel
        dp = [0] + [-1 for _ in range(days[0], days[-1]+1)]
        
        for day in days:
            dp[day-days[0]+1] = 0 # initialized to 0 for traverling days
        
        # dp starts here, we will look back to see because the best choice of today depends on the future days
        for i in range(1, len(dp)):
            if dp[i] == -1: # today is not traveling day
                dp[i] = dp[i - 1] # no extra cost
            else: # today is traveling day
                # compute optimal cost by DP
                one = dp[max(i-1, 0)] + costs[0] # look back one day, what's the cost if we purchase a 1 day ticket yesterday?
                seven = dp[max(i-7, 0)] + costs[1] # look back 7 days, what's the cost if we purchase a 7 day ticket 7 days ago?
                thirty = dp[max(i-30, 0)] + costs[2] # look back 30 days, what's the cost if we purchase a 30 day ticket 30 days ago?
                dp[i] = min(one, seven, thirty)
    
        return dp[-1]
        
        
if __name__ == '__main__':
    solver = Solution()
    days = [14,16,17,19,21,22]
    costs = [1,4,18]
    print(solver.mincostTicketsDPFromStart(days, costs))

