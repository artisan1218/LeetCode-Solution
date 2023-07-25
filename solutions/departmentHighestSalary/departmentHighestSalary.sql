-- solution 1
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


-- solution 2
SELECT 
  D.name AS Department,
  E.name AS Employee,
  E.salary AS Salary
FROM Employee AS E LEFT JOIN Department AS D ON E.departmentId = D.id
WHERE salary = (
  SELECT MAX(salary) FROM Employee WHERE departmentId = E.departmentId
);