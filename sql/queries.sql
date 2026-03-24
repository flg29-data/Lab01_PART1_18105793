-- MÉTRICAS DE NEGÓCIO

-- 1. Receita total

SELECT SUM(total_cost) FROM fact_sales;


-- 2. Produto mais vendido

SELECT product, SUM(total_cost)
FROM fact_sales
GROUP BY product
ORDER BY 2 DESC
LIMIT 10;


-- 3. Receita por país

SELECT city, SUM(total_value)
FROM fact_sales
GROUP BY city;


-- 4. Crescimento mensal

SELECT DATE_TRUNC('month', date), SUM(total_cost)
FROM fact_sales
GROUP BY 1
ORDER BY 1;


-- 5. Ticket médio por cliente

SELECT customer_name, AVG(total_cost)
FROM fact_sales
GROUP BY customer_name;
