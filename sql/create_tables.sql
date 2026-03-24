
-- CRIAR TABELAS DE DIMENSAO

CREATE TABLE dim_product (
    product_id SERIAL PRIMARY KEY,
    product TEXT
);

CREATE TABLE dim_customer (
    customer_name TEXT PRIMARY KEY,
    city TEXT
);

CREATE TABLE dim_date (
    date_id DATE PRIMARY KEY,
    year INT,
    month INT
);


-- CRIAR TABELA DE FATO

CREATE TABLE fact_sales (
    id SERIAL PRIMARY KEY,
    customer_name TEXT,
    product TEXT,
    total_itens FLOAT,
    total_cost FLOAT,
    date DATE
);
