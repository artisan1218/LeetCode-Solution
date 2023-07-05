# Combine Two Tables problem
![image](https://github.com/artisan1218/LeetCode-Solution/assets/25105806/c387c9c3-4843-40d0-ba15-dbf56f21e58d)



Leetcode link: https://leetcode.com/problems/combine-two-tables/description/

<br />

### Approach 1: Left Join

Since not all person in Address table has a corresponding address, and in such cases we should put NULL, we can use a left join to combine these two tables. `Person` table will be the left table and `Address` will be the right table.

```sql
SELECT 
  Person.firstName,
  Person.lastName,
  Address.city,
  Address.state
FROM Person 
LEFT JOIN Address
ON Person.personId = Address.personId
```

Running Time:
![image](https://github.com/artisan1218/LeetCode-Solution/assets/25105806/6eded3b1-5428-428c-a707-e7a8cab497c1)
