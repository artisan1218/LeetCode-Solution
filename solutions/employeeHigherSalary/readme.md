# Employees Earning More Than Their Managers problem
![image](https://github.com/artisan1218/LeetCode-Solution/assets/25105806/c8c0d30d-1f60-467d-a164-65afb96530c4)

Leetcode link: https://leetcode.com/problems/employees-earning-more-than-their-managers

<br />

### Approach 1: 

Since we're going to compare employee's salary with corresponding manger's salary, we can just ensure such condition in the where clause. Manager's salary can be found by another sub-query:

```sql
SELECT e.name AS Employee
FROM Employee AS e
WHERE e.salary > (SELECT m.salary FROM Employee AS m WHERE m.id = e.managerId);
```

This is not the optimal solution because apparently we're doing n^2 comparisons: for each employee, we have to find it's manager's salary. 

Running time:
![image](https://github.com/artisan1218/LeetCode-Solution/assets/25105806/5603b996-ed95-4438-9031-53ab8c8c14e5)


<br />

### Approach 2:

Instead of finding manager's salary in a sub-query, we can simply join employee table with manager table (although they are the same table) to get employee's manager and manager's salary:

```sql
SELECT e.name AS Employee
FROM Employee AS e LEFT JOIN Employee AS m ON e.managerId = m.id
WHERE e.salary > m.salary;
```

Running time:
![image](https://github.com/artisan1218/LeetCode-Solution/assets/25105806/e87f9cd2-3df7-40d8-8e09-62b22e570275)
