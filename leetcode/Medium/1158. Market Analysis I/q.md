# Question

- `SQL Schema`
    
    ```sql
    Create table If Not Exists Users (user_id int, join_date date, favorite_brand varchar(10))
    Create table If Not Exists Orders (order_id int, order_date date, item_id int, buyer_id int, seller_id int)
    Create table If Not Exists Items (item_id int, item_brand varchar(10))
    Truncate table Users
    insert into Users (user_id, join_date, favorite_brand) values ('1', '2018-01-01', 'Lenovo')
    insert into Users (user_id, join_date, favorite_brand) values ('2', '2018-02-09', 'Samsung')
    insert into Users (user_id, join_date, favorite_brand) values ('3', '2018-01-19', 'LG')
    insert into Users (user_id, join_date, favorite_brand) values ('4', '2018-05-21', 'HP')
    Truncate table Orders
    insert into Orders (order_id, order_date, item_id, buyer_id, seller_id) values ('1', '2019-08-01', '4', '1', '2')
    insert into Orders (order_id, order_date, item_id, buyer_id, seller_id) values ('2', '2018-08-02', '2', '1', '3')
    insert into Orders (order_id, order_date, item_id, buyer_id, seller_id) values ('3', '2019-08-03', '3', '2', '3')
    insert into Orders (order_id, order_date, item_id, buyer_id, seller_id) values ('4', '2018-08-04', '1', '4', '2')
    insert into Orders (order_id, order_date, item_id, buyer_id, seller_id) values ('5', '2018-08-04', '1', '3', '4')
    insert into Orders (order_id, order_date, item_id, buyer_id, seller_id) values ('6', '2019-08-05', '2', '2', '4')
    Truncate table Items
    insert into Items (item_id, item_brand) values ('1', 'Samsung')
    insert into Items (item_id, item_brand) values ('2', 'Lenovo')
    insert into Items (item_id, item_brand) values ('3', 'LG')
    insert into Items (item_id, item_brand) values ('4', 'HP')
    ```
    

Table: `Users`

```
+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| user_id        | int     |
| join_date      | date    |
| favorite_brand | varchar |
+----------------+---------+
user_id is the primary key of this table.
This table has the info of the users of an online shopping website where users can sell and buy items.

```

Table: `Orders`

```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| order_id      | int     |
| order_date    | date    |
| item_id       | int     |
| buyer_id      | int     |
| seller_id     | int     |
+---------------+---------+
order_id is the primary key of this table.
item_id is a foreign key to the Items table.
buyer_id and seller_id are foreign keys to the Users table.

```

Table: `Items`

```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| item_id       | int     |
| item_brand    | varchar |
+---------------+---------+
item_id is the primary key of this table.

```

Write an SQL query to find for each user, the join date and the number of orders they made as a buyer in `2019`.

Return the result table in **any order**.

The query result format is in the following example.

**Example 1:**

```
Input:
Users table:
+---------+------------+----------------+
| user_id | join_date  | favorite_brand |
+---------+------------+----------------+
| 1       | 2018-01-01 | Lenovo         |
| 2       | 2018-02-09 | Samsung        |
| 3       | 2018-01-19 | LG             |
| 4       | 2018-05-21 | HP             |
+---------+------------+----------------+
Orders table:
+----------+------------+---------+----------+-----------+
| order_id | order_date | item_id | buyer_id | seller_id |
+----------+------------+---------+----------+-----------+
| 1        | 2019-08-01 | 4       | 1        | 2         |
| 2        | 2018-08-02 | 2       | 1        | 3         |
| 3        | 2019-08-03 | 3       | 2        | 3         |
| 4        | 2018-08-04 | 1       | 4        | 2         |
| 5        | 2018-08-04 | 1       | 3        | 4         |
| 6        | 2019-08-05 | 2       | 2        | 4         |
+----------+------------+---------+----------+-----------+
Items table:
+---------+------------+
| item_id | item_brand |
+---------+------------+
| 1       | Samsung    |
| 2       | Lenovo     |
| 3       | LG         |
| 4       | HP         |
+---------+------------+
Output:
+-----------+------------+----------------+
| buyer_id  | join_date  | orders_in_2019 |
+-----------+------------+----------------+
| 1         | 2018-01-01 | 1              |
| 2         | 2018-02-09 | 2              |
| 3         | 2018-01-19 | 0              |
| 4         | 2018-05-21 | 0              |
+-----------+------------+----------------+
```

# Answer

```sql
SELECT
	users.user_id AS buyer_id
    , users.join_date AS join_date
    , COALESCE(orders.cnt,0) AS orders_in_2019
FROM users
LEFT JOIN 
(   
	SELECT 
		buyer_id
		, count(order_date) AS cnt
	FROM orders
	WHERE SUBSTRING(order_date, 1, 4) = 2019
	GROUP BY buyer_id
) AS orders ON users.user_id = orders.buyer_id;
```

## 실행 결과

![Untitled](../../../image/leetcode/1158_Market_Analysis_I/image.png)