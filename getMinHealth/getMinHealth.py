import heapq

def getMinHealth(initPlayers, nextPlayers, rank):
    result = []
    heap = []
    heapq.heapify(heap) # make a heap
    
    # only keep the top 'rank' players in heap
    for init_hp in initPlayers:
        if len(heap) < rank:
            heapq.heappush(heap, init_hp)
        elif heap[0] < init_hp:
            heapq.heappop(heap)
            heapq.heappush(heap, init_hp)
    
    result.append(heap[0]) # initial hp
  
    for next_hp in nextPlayers:
        if next_hp > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, next_hp)
        result.append(heap[0])
    
    return sum(result)
   
    
if __name__ == "__main__":
    initPlayers = [1, 2]
    nextPlayers = [3, 4]
    rank = 2
    getMinHealth(initPlayers, nextPlayers, rank)
# In[ ]:




