-- solution 1
SELECT DISTINCT(p1.Email) AS Email
FROM Person AS p1, Person AS p2
WHERE p1.id != p2.id AND p1.email = p2.email;

-- solution 2
SELECT email
FROM Person
GROUP BY email
HAVING COUNT(email) > 1;