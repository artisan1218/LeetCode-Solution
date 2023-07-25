# Department Top Three Salaries problem

![image](https://github.com/artisan1218/LeetCode-Solution/assets/25105806/430fa10a-8528-41d5-a1ce-c9b867c43cfb)
![image](https://github.com/artisan1218/LeetCode-Solution/assets/25105806/52ea338f-ff33-4305-8fcc-114641a9b5c0)


Leetcode link: https://leetcode.com/problems/department-top-three-salaries

<br />

### Approach 1: DENSE_RANK()

Similar to problem [Department Highest Salary](https://github.com/artisan1218/LeetCode-Solution/tree/main/solutions/departmentHighestSalary), we can use some sort of ranking function to get the salary ranking in each department, then simply choose top 3 salaries. Since we want the ranking to be continuous, we use `DENSE_RANK()`.

```sql
SELECT Employee, Salary, Department
FROM (
    SELECT 
    E.name AS Employee,
    E.Salary AS Salary,
    D.name AS Department,
    DENSE_RANK() OVER (PARTITION BY D.name ORDER BY E.salary DESC) AS Ranking 
    FROM Employee AS E LEFT JOIN Department AS D ON E.departmentId = D.id
) AS temp
WHERE temp.Ranking <= 3;
```

Running time:
![image](https://github.com/artisan1218/LeetCode-Solution/assets/25105806/57c9a760-0526-4dbf-ab44-89ac5ff36414)


<br />

### Approach 2: Sub-Query

We can achieve the same result using sub-query. The sub-query basically answer the question of "how many salaries are higher than current salary?". The use of `DISTINCT()` is to make sure two same salaries are treated as one salary otherwise we will have different ranking for same salary.

```sql
SELECT 
  E.name AS Employee,
  E.Salary AS Salary,
  D.name AS Department
FROM Employee AS E LEFT JOIN Department AS D ON E.departmentId = D.id
WHERE (
  SELECT COUNT(DISTINCT(salary))
  FROM Employee AS E2
  WHERE E.salary < E2.salary AND E.departmentId = E2.departmentId
) < 3;
```

Running time:
![image](https://github.com/artisan1218/LeetCode-Solution/assets/25105806/10dc3b08-a151-4a86-a829-f1d5768c7306)
