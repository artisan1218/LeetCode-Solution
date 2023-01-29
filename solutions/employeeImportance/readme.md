# Employee Importance problem
![image](https://user-images.githubusercontent.com/25105806/136710277-24fc2138-57cf-44a5-85d2-504a8cd699dd.png)

Leetcode link: https://leetcode.com/problems/employee-importance/

<br />

### Approach 1: BFS, getImportanceBFS()
The data structure of `Employee` can be seen as a tree structure. We can simply use BFS to explore the tree and sum up all importance. We use a stack `subord` to store all nodes that are waiting to be explored. We just need to build a look up table `lookup` to speed up the retrieval based on employee's `id`

```python
def getImportanceBFS(self, employees: List['Employee'], id: int) -> int:
    lookup = dict()
    for emp in employees:
        lookup[emp.id] = (emp.importance, emp.subordinates)

    subord = lookup[id][1]
    result = lookup[id][0]

    while len(subord)!=0:
        emp = subord.pop()
        result += lookup[emp][0]
        subord += lookup[emp][1]

    return result
```

Time complexity is O(n) where n is the length of `employees`:
![image](https://user-images.githubusercontent.com/25105806/136710377-f0fec9d7-d817-4020-86c8-c8f1992162ee.png)

<br />

### Approach 2: DFS, getImportanceDFS()
Since it is a tree structure, we can also use DFS to solve this. We just need to build a look up table `lookup` to speed up the retrieval based on employee's `id`

```python
def dfs(lookup, id):
    result = lookup[id][0]
    for i in lookup[id][1]:
        result += dfs(lookup, i)
    return result

    lookup = dict()
    for emp in employees:
        lookup[emp.id] = (emp.importance, emp.subordinates)
    return dfs(lookup, id)
```

Time complexity is O(n) where n is the length of `employees`:\
![image](https://user-images.githubusercontent.com/25105806/136710443-61bbc228-d605-44e9-829b-0131ea2b4b6d.png)

