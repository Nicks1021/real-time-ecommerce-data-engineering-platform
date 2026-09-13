-- 1. Total Orders
SELECT COUNT(*) AS total_orders
FROM orders;


-- 2. Total Sales
SELECT SUM(total_amount) AS total_sales
FROM orders;


-- 3. Average Order Value
SELECT AVG(total_amount) AS average_order_value
FROM orders;


-- 4. Product-wise Sales
SELECT
    product,
    COUNT(*) AS total_orders,
    SUM(total_amount) AS total_sales
FROM orders
GROUP BY product
ORDER BY total_sales DESC;


-- 5. City-wise Sales
SELECT
    city,
    COUNT(*) AS total_orders,
    SUM(total_amount) AS total_sales
FROM orders
GROUP BY city
ORDER BY total_sales DESC;