# Nth Highest Salary problem
![image](https://github.com/artisan1218/LeetCode-Solution/assets/25105806/661c5369-e128-4950-a00c-e818c3d1f8cf)

Leetcode link: https://leetcode.com/problems/nth-highest-salary/

<br />

### Approach 1: ORDER BY

Since we want the Nth salary, we should think of sorting the table, then take the Nth row from the beginning, which can be done by using `LIMIT` and offset

```sql
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
SET N = N-1;
  RETURN (
    SELECT DISTINCT(salary) AS salary
    FROM Employee
    ORDER BY salary DESC
    LIMIT N, 1
  );
END
```

Running time:
![image](https://github.com/artisan1218/LeetCode-Solution/assets/25105806/8ebeb548-2623-4f41-a894-5e6afe7f9930)
