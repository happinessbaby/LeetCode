# Write your MySQL query statement below
# select temp.customer_number from (select customer_number, count(*) as "order_count" from Orders group by customer_number order by order_count desc limit 1) temp
select customer_number from orders group by customer_number order by count(*) desc limit 1