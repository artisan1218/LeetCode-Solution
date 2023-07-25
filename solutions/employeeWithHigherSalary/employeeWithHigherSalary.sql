-- solution 1
SELECT e.name AS Employee
FROM Employee AS e
WHERE e.salary > (SELECT m.salary FROM Employee AS m WHERE m.id = e.managerId);

-- solution 2
SELECT e.name AS Employee
FROM Employee AS e LEFT JOIN Employee AS m ON e.managerId = m.id
WHERE e.salary > m.salary;