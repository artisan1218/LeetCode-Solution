#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from typing import List

# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution:
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
    
    def getImportanceDFS(self, employees: List['Employee'], id: int) -> int:
        def dfs(lookup, id):
            result = lookup[id][0]
            for i in lookup[id][1]:
                result += dfs(lookup, i)
            return result
        
        lookup = dict()
        for emp in employees:
            lookup[emp.id] = (emp.importance, emp.subordinates)
        return dfs(lookup, id)
    

