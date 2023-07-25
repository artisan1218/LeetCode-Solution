-- solution 1
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

-- solution 2
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