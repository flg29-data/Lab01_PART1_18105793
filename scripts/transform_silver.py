import pandas as pd

df = pd.read_csv("data/raw/raw/retail_raw.csv")

# Padronizar nomes
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(' ', '_')
)

# Converter data
df['date'] = pd.to_datetime(df['date'])

# Criar métricas
df['total_value'] = df['total_items'] * df['total_cost']

# Tratar nulos
df['customer_name'] = df['customer_name'].fillna("UNKNOWN")
df['promotion'] = df['promotion'].fillna("UNKNOWN")

# Remover valores inválidos
df = df[df['total_items'] > 0]
df = df[df['total_cost'] > 0]

# Remover duplicados
df = df.drop_duplicates()

# Salvar Parquet
df.to_parquet("data/silver/retail_silver.parquet", index=False)

print("Silver pronto")
