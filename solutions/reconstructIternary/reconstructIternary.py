#!/usr/bin/env python
# coding: utf-8

# In[1]:


from typing import List

class Solution:
    def findItineraryBacktrack(self, tickets: List[List[str]]) -> List[str]:
        # construct adj list
        tickets.sort()
        adj = {pair[0]:[] for pair in tickets}
        for src, dst in tickets:
            adj[src].append(dst)
        
        result = ['JFK'] # result always start with JFK
        def helper(cur):
            # we have found a solution
            if len(result) == len(tickets) + 1:
                return True
            elif cur not in adj: # current src does not have any outgoing flights
                return False
            else:
                temp = list(adj[cur])
                for i, next in enumerate(temp):
                    adj[cur].pop(i) # remove current src from available flights so that we don't use it again
                    result.append(next) # go to this airport
                    if helper(next): 
                        return True
                    else: # if this path does not lead to a solution, we backtrack the previous path
                        # backtracking
                        adj[cur].insert(i, next) # add src back to available flights
                        result.pop() 
                return False # this is not needed because "You may assume all tickets form at least one valid itinerary."

        helper('JFK')
        return result 

    def findItineraryIteration(self, tickets: List[List[str]]) -> List[str]:
        # construct adj list
        tickets.sort()
        adj = {pair[0]:[] for pair in tickets}
        for src, dst in tickets:
            adj[src].append(dst)

        result = []
        stack = ['JFK']
        while len(stack)!=0:
            if stack[-1] not in adj or len(adj[stack[-1]])==0:
                # if a src airport does not have any outgoing flights, then that means this is the airport that we should visit at the last
                # because it can not offer a flight back, we can simply pop this out to the result and return the reversed result
                result.append(stack.pop()) 
            else:
                next = adj[stack[-1]].pop(0)
                stack.append(next)

        return result[::-1]



if __name__ == '__main__':
    tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
    solver = Solution()
    result = solver.findItineraryIteration(tickets)
    print(result)

