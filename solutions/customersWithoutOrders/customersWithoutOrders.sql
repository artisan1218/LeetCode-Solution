-- solution 1
SELECT C.name AS Customers
FROM Customers AS C LEFT JOIN Orders AS O ON C.id = O.customerId
WHERE O.customerId IS NULL;

-- solution 2
SELECT name AS Customers
FROM Customers
WHERE id NOT IN (SELECT customerId FROM Orders);