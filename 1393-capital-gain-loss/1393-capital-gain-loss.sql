# Write your MySQL query statement below
# select temp3.stock_name, temp3.sell_total-temp3.buy_total as "capital_gain_loss" from ((select stock_name, sum(price) as "sell_total" from Stocks where operation = "Sell" group by stock_name) temp1 join 
# (select stock_name, sum(price) as "buy_total" from Stocks where operation="Buy" group by stock_name) temp2 on temp1.stock_name = temp2.stock_name )) temp3
 
select stock_name, temp1.sell_total - temp2.buy_total as "capital_gain_loss" from (select stock_name, sum(price) as "sell_total" from Stocks where operation = "Sell" group by stock_name) temp1
join 
(select stock_name, sum(price) as "buy_total" from Stocks where operation="Buy" group by stock_name) temp2
using (stock_name)
group by stock_name

