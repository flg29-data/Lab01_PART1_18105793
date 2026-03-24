# Lab01_PART1_NUSP_18105793

# LABORATÓRIO 01-A: Ingestão de Dados End-to-End (Local) 

# Fernando Luiz Gomes - NUSP 18105793

**Disciplina:** Fundamentos de Engenharia de Dados  

## Objetivo

Este laboratório tem como propósito a construção de um Pipeline (Engenharia de Dados), com a arquitetura em camadas: Raw, Bronze, Silver e Gold, com objetivo na ingestão, tratamento e preparo dos dados de transações do varejo (análise de cesta de compras, segmentação de clientes e análise de varejo).

## DATASET

- **Nome:** Brazilian E-Commerce Public Dataset (Olist)
- **Fonte:** Kaggle
- **Dataset:** Retail Transactions Dataset
- **Arquivo Utilizado:** Retail_Transactions_Dataset.csv
- **Volume:** 1.000.000 registros e 13 colunas 

## Conteúdo

## 1. [Arquitetura]

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

## 2. [Documentação da tarefa]

### 2.1 [Camada Raw]

Salvar o dataset sem nenhuma transformação, mantendo os dados no formato original


→ python no script >> `scripts/ingest_raw.py`


### 2.2 [Camada Silver]

Tratamento dos dados:
- padronização dos nomes
- conversão dos dados
- criação de métricas
- tratamento de nulos
- remover valores inválidos
- remover valores duplicados


→ python no script >> `scripts/transform_silver.py`


### 2.3 [Camada Gold]

Modelagem no PostgreSQL

Criação das Tabelas
1 Fato (fact_sales)
3 Dimensões (dim_product, dim_customer, dim_date)

→ query SQL >> `sql/create_tables.sql`

Carregamento dos dados PARQUET para PostgreSQL via Python

→ python no script >> `scripts/load_gold.py`


## 3. [Dicionário de Dados]


## 4. [Qualidade de Dados]


## 5. [Instruções de Execução]
