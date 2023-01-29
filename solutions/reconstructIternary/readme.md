# Reconstruct Itinerary problem
<img width="852" alt="image" src="https://user-images.githubusercontent.com/25105806/145752263-5c32fcff-db7a-4276-bd37-ddbbb5980c91.png">
<img width="976" alt="image" src="https://user-images.githubusercontent.com/25105806/145752301-08406c51-177e-417c-b888-d132d9bb29c8.png">

Leetcode link: https://leetcode.com/problems/reconstruct-itinerary/

<br/>


### Approach 1: Backtracking, findItineraryBacktrack()
Credits to: https://www.youtube.com/watch?v=ZyB_gQ8vqGA

This key idea is to use backtracking to explore the all paths and going back when a path does not lead to final solution. We first need to construct adjacency list to store all available flights in the map. Then simply use current `src` airport to find the next airport in adjacency list. 

The below example shows a case where a lexically lower airport does not lead to final solution (there is no outgoing airport at B). Thus we should go to `C` first instead of `B` even though `B` is lexically lower than `C`.
<img src="https://user-images.githubusercontent.com/25105806/145752708-2ed00507-a8b8-49a8-8017-062424d77981.jpeg" width="50%" height="50%">

```python
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
```

Time complexity is O(n^2) where n is the number of airports:\
<img width="691" alt="image" src="https://user-images.githubusercontent.com/25105806/145753033-aabaa900-b600-45b7-93a6-9a475b24ee0b.png">


<br />

### Approach 2: Stack, findItineraryIteration()
Credits to: https://www.youtube.com/watch?v=WYqsg5dziaQ

We can also use stack to solve this question. The key point is to use stack to solve the problem of 'backtracking'. If a src airport does not have any outgoing flights, then that means this is the airport that we should visit at the last. Because it can not offer a flight back, we can simply pop this out to the result and return the reversed result.

```python
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
```

Time complexity is O(n):\
<img width="708" alt="image" src="https://user-images.githubusercontent.com/25105806/145753251-130a974e-a0d8-4229-a6ec-43fb76e39f4a.png">

                



