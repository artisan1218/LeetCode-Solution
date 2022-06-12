# Shortest Rainbow Path problem

<img src="https://user-images.githubusercontent.com/25105806/173221324-af828e3c-a826-4497-86fe-d5078873bf19.jpg" height="70%" width="70%">

<br />

### Approach 1: Dijkstra's Algorithm

Since we're calculating the shortest path of a positive weighted directed graph, it's easy to think of using Dijkstra's algorithm. However, we need to account for additional condition "color of the node" when selecting the next node to visit. The core of Dijkstra's algorithm is to use BFS to expand the neighbor nodes and calculating path weight sum and priority queue to select the next node with minimum edge weight (plus any additional condition such as color).


Full code consists of the implementation of the standard Dijkstra's algorithm and a modified Dijkstra's algorithm for this problem.

Standard Dijkstra's algorithm:
```python3
def reconstructPath(path, start, end):
    result = []
    while end != start:
        result.append(end)
        end = path[end]
    result.append(start)
    return result[::-1]

def findNextVertex(dist, visited):
    result = None
    minDist = float('inf')
    for v, d in dist.items():
        if d < minDist and v not in visited:
            minDist = d
            result = v
    return result

def dijkstra(graph, start):
    # initialize all distance to inf
    dist = {}
    for v in graph.keys():
        dist[v] = float('inf')
    dist[start] = 0
    
    # initialize the path
    path = {}
    for v in graph.keys():
        path[v] = None
    
    visited = set()
    while len(visited) != len(graph):
        v = findNextVertex(dist, visited)
        visited.add(v)
        for neighbor, d in graph[v].items():
            if neighbor not in visited and d+dist[v] < dist[neighbor]:
                dist[neighbor] = d + dist[v]
                path[neighbor] = v
    return dist, path
```

<br />

Modified Dijkstra's algorithm
```python3
def dijkstraColor(graph, color, start):
    # initialize all distance to inf
    dist = {}
    for v in graph.keys():
        dist[v] = float('inf')
    dist[start] = 0
    
    # initialize the path
    path = {}
    for v in graph.keys():
        path[v] = None
    
    visited = set()
    while len(visited) != len(graph):
        v = findNextVertex(dist, visited)
        visited.add(v)
        for neighbor, d in graph[v].items():
            if neighbor not in visited and d+dist[v] < dist[neighbor] and color[neighbor]!=color[v]:
                dist[neighbor] = d + dist[v]
                path[neighbor] = v
    return dist, path
```

Time complexity is the same as standard Dijkstra's algorithm because the color checking is a O(1) operation: O(e + vlogv) where e is the number of edges in the graph and v is the number of vertices in the graph.
