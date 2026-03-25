# Lab01_PART1_NUSP_18105793

# LABORATÓRIO 01-A: Ingestão de Dados End-to-End (Local) 

# Fernando Luiz Gomes - NUSP 18105793

**Disciplina:** Fundamentos de Engenharia de Dados  

## Objetivo

Este laboratório tem como propósito a construção de um Pipeline (Engenharia de Dados), com a arquitetura em camadas: Raw, Bronze, Silver e Gold, com objetivo na ingestão, tratamento e preparo dos dados de transações do varejo (análise de cesta de compras, segmentação de clientes e análise de varejo).

Link GitHub >> https://github.com/flg29-data/Lab01_PART1_18105793

## DATASET

- **Nome:** Brazilian E-Commerce Public Dataset (Olist)
- **Fonte:** Kaggle
- **Dataset:** Retail Transactions Dataset
- **Arquivo Utilizado:** Retail_Transactions_Dataset.csv
- **Volume:** 1.000.000 registros e 13 colunas 

## Conteúdo

## 1. Arquitetura

Construção do Pipeline

```
→ CSV (Kaggle) - 1M Registros
  - Importação Carga >> Arquivo: Retail_Transactions_Dataset.csv

→ Python (versão 3.14.3)
  - Instalação bibliotecas >> pip install pandas sqlalchemy psycopg2-binary

→ Parquet
  - Instalação >> ppip install fastparquet

→ Gráficos Python
  - Instalação Biblioteca >> pip install matplotlib

→ PostgreSQL (versão 18.3)
  - Instalação >> configuração da Porta 5432 >> pgAdmin
  - Configuração Database >> CREATE DATABASE lab_data;
```

## 2. Documentação da tarefa

### 2.1 Camada Raw

Salvar o dataset sem nenhuma transformação, mantendo os dados no formato original

→ python no script >> `scripts/ingest_raw.py`

**RESULTADO**

![RESULTADO](images/ingest_raw.png)


### 2.2 Camada Silver

#### 2.2.1 Tratamento dos dados:

- Dados tratados (padronização campos, datas, métricas, nulos e duplicados)
- Criação do arquivo PARQUET

→ python no script >> `scripts/transform_silver.py`

**RESULTADO**

![RESULTADO](images/transform_silver.png)

#### 2.2.2 Construção dos gráficos:

Construção dos graficos separados por:

- Receita por pais (barra horizontal)
- Top produtos (coluna vertical)
- Receita por mês (linha)
- Distribuição de preços (histograma)
- Ticket médio por cliente (pizza)

Instalação da biblioteca >>  ```pip install matplotlib```

**RESULTADO**

![install_matplotlib](images/install_matplotlib.png)

→ python no script >> `scripts/graficos.py`

**RESULTADO**

![Graficos](images/graficos.png)

## GRÁFICOS GERADOS 

### 1. Receita por país
**RESULTADO**

![Receita por país](images/grafico1_barra_horizontal.png)

### 2. Top produtos
**RESULTADO**

![Top produtos](images/grafico2_coluna_vertical.png)

### 3. Receita por mês
**RESULTADO**

![Receita por mês](images/grafico3_linha.png)

### 4. Distribuição de preços
**RESULTADO**

![Distribuição de preços](images/grafico4_histograma.png)

### 5. Ticket médio por cliente
**RESULTADO**

![Ticket médio por cliente](images/grafico5_pizza.png)

### 2.3 Camada Gold

#### 2.3.1 Modelagem no PostgreSQL

Criação das Tabelas:
- 1 Fato (fact_sales)
- 3 Dimensões (dim_product, dim_customer, dim_date)

→ query SQL >> `sql/create_tables.sql`

**RESULTADO**

![RESULTADO](images/sql_create_tables.png)

#### 2.3.2 Definição das Metricas de negócio (dados de transações do varejo)

Construção das regras de negócio separando por:
- Receita Total
- Produto mais vendido
- Receita por país
- Crescimento mensal
- Ticket médio por cliente

→ query SQL >> `sql/queries.sql`

#### 2.3.3 Carregamento dos dados PARQUET para PostgreSQL via Python

→ python no script >> `scripts/load_gold.py`

**RESULTADO**

![RESULTADO](images/load_gold.png)



## CONSULTAS GERADAS

### 1. Receita Total
**RESULTADO**

![Receita Total](images/sql_receita_total.png)

### 2. Produto mais vendido
**RESULTADO**

![Produto mais vendido](images/sql_produto_vendido.png)

### 3. Receita por país
**RESULTADO**

![Receita por país](images/sql_receita_pais.png)

### 4. Crescimento mensal
**RESULTADO**

![Crescimento mensal](images/sql_crescimento_mensal.png)

### 5. Ticket médio por cliente
**RESULTADO**

![Ticket médio por cliente](images/sql_ticket_cliente.png)


## 3. Dicionário de Dados

*Dicionário de dados construído*

#### `fact_sales`

| Coluna                   | Tipo      | Descrição |
|--------------------------|----------|----------|
| `transaction_id`             | bigint  | Campo Id transação |
| `date`             | timestamp  | Campo data|
| `customer_name`            | text  | Campo nome cliente  |
| `product`             | text  | Campo produto |
| `total_itens`            | bigint  | Campo total itens venda |
| `total_cost`             | double precision  | Campo total soma vendas |
| `payment_method`             | text  | Campo metodo de pagamento |
| `city`             | text  | Campo cidade |
| `store_type`             | text  | Campo tipo de loja |
| `discount_applied`             | boolean  | Campo desconto aplicado |
| `customer_applied`             | boolean  | Campo consumidor aplicado |
| `season`             | text  | Campo sazonalidade |
| `promotion`             | text  | Campo promocao produtos |
| `total_value`             | double precision  | Campo valor total |


#### `dim_customer`

| Coluna                   | Tipo      | Descrição |
|--------------------------|----------|----------|
| `customer_name`             | text  | Campo nome cliente |
| `city`             | text  | Campo cidade |


#### `dim_date`

| Coluna                   | Tipo      | Descrição |
|--------------------------|----------|----------|
| `date_id`             | date  | Campo Id data |
| `year`             | int  | Campo ano |
| `month`             | int  | Campo mes |


#### `dim_product`

| Coluna                   | Tipo      | Descrição |
|--------------------------|----------|----------|
| `product_id`             | int  | Campo Id produto |
| `product`             | text  | Campo nome produto |



## 4. Qualidade de Dados

### 4.1 Tratamentos realizados (Camada Silver)

- padronização dos nomes das colunas
- conversão dos dados
- criação de métricas
- tratamento de nulos
- remover valores inválidos
- remover valores duplicados

## 5. Instruções de Execução

Execução realizada:

```
pip install -r requirements.txt

python scripts/ingest_raw.py
python scripts/transform_silver.py
python scripts/load_gold.py
```
