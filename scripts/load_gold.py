import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("postgresql://postgres:postgres@localhost:5432/lab_data")

df = pd.read_parquet("C:/Users/ferna/OneDrive/Laboratorio01/silver/retail_silver.parquet")

df.to_sql("fact_sales", engine, if_exists="replace", index=False)

print("Dados carregados no Postgres")
