# Department Highest Salary problem
![image](https://github.com/artisan1218/LeetCode-Solution/assets/25105806/58ab4fe3-2592-4349-b057-cf62573224ca)
![image](https://github.com/artisan1218/LeetCode-Solution/assets/25105806/b6850bfd-3d27-4277-ae27-2957d45908c9)



Leetcode link: https://leetcode.com/problems/department-highest-salary/description/

<br />

### Approach 1: RANK()

We want the top salary per department, then it's straightforward to rank the salaries per department. We can utilize the `RANK()` function to achieve this. First join two tables together to get the department name, then rank the salary per department:

```sql
SELECT Employee, Salary, Department
FROM (
    SELECT 
    E.name AS Employee,
    E.Salary AS Salary,
    D.name AS Department,
    RANK() OVER (PARTITION BY D.name ORDER BY E.salary DESC) AS Ranking 
    FROM Employee AS E LEFT JOIN Department AS D ON E.departmentId = D.id
) AS temp
WHERE temp.Ranking = 1;
```

Running time:
![image](https://github.com/artisan1218/LeetCode-Solution/assets/25105806/88239f99-ab31-4593-aa79-45910dc5ce3a)


<br />

### Approach 2: Sub-Query

Instead of using `RANK()`, we can also use a sub-query to get the highest salry per department, but still need to join two tables together to get the department name:

```sql
SELECT
  D.name AS Department,
  E.name AS Employee,
  E.salary AS Salary
FROM Employee AS E LEFT JOIN Department AS D ON E.departmentId = D.id
WHERE salary = (
  SELECT MAX(salary) FROM Employee WHERE departmentId = E.departmentId
);
```

Running time:
![image](https://github.com/artisan1218/LeetCode-Solution/assets/25105806/cc86ea98-1c3f-43b8-b4fb-5c0ac9d8c21d)
