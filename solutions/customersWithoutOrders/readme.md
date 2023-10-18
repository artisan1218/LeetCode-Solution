# Customers Who Never Order problem
![image](https://github.com/artisan1218/LeetCode-Solution/assets/25105806/0fe7ca0e-6492-4436-a8af-f1ba056be79a)
![image](https://github.com/artisan1218/LeetCode-Solution/assets/25105806/02ea5426-d47d-4298-a2f5-e26bc24e14d6)



Leetcode link: https://leetcode.com/problems/customers-who-never-order

<br />

### Approach 1: 

We can simply join two tables together on the customer ID and in `Orders` table, find the rows with NULL `customerId`

```sql
SELECT C.name AS Customers
FROM Customers AS C LEFT JOIN Orders AS O ON C.id = O.customerId
WHERE O.customerId IS NULL;
```

Running time:
![image](https://github.com/artisan1218/LeetCode-Solution/assets/25105806/2682fd8a-3160-495b-9a9e-c8419139fe57)


<br />

### Approach 2: 

Instead of joining two tabels, we can simply use a sub-query to see if a customer has any orders in `Orders`

```sql
SELECT name AS Customers
FROM Customers
WHERE id NOT IN (SELECT customerId FROM Orders);
```


Running time:
![image](https://github.com/artisan1218/LeetCode-Solution/assets/25105806/a203ad45-1fdd-426b-8740-04c43b0ddc98)
