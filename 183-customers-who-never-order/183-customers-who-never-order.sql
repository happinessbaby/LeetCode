# Write your MySQL query statement below
# SELECT name as "Customers" FROM Customers WHERE id NOT IN (SELECT customerid FROM Orders)
SELECT name as "Customers" FROM Customers LEFT JOIN Orders ON Customers.id=Orders.customerId WHERE Orders.customerId IS NULL

