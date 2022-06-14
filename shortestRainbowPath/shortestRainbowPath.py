#!/usr/bin/env python
# coding: utf-8

# <div>
# <img src="attachment:shortestRainbowPathProblemStatement.png" width="60%" height="60%"/>
# </div>

# In[2]:


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

# above is standard dijkstra's algorithm
#------------------------------------------------------------------------------------
# below is dijkstra's algorithm with color feature

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


# In[3]:


if __name__ == "__main__":
    graph = {
        'a':{'b':4, 'c':2},
        'b':{'a':4, 'c':3, 'd':1},
        'c':{'a':2, 'b':3, 'd':5},
        'd':{'b':1, 'c':5}
    }
    color = {
        'a':'turquoise',
        'b':'red',
        'c':'turquoise',
        'd':'yellow'
    }
    
    dist, allPath = dijkstraColor(graph, color, 'a')
    resultPath = reconstructPath(allPath, 'a', 'c')
    
    print('Reconstructed path is:', resultPath)

