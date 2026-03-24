import pandas as pd
import matplotlib.pyplot as plt

# Carregar dados
df = pd.read_parquet("C:/Users/ferna/OneDrive/Laboratorio01/silver/retail_silver.parquet")

# Garantir tipo datetime
df['date'] = pd.to_datetime(df['date'])

# ================================
# 1. GRÁFICO DE BARRAS (horizontal)
# Receita por cidade
# ================================
plt.figure(figsize=(12, 8))
plt.xticks(fontsize=8)
df.groupby("city")["total_value"].sum().sort_values().plot(kind="barh")
plt.title("Receita por Cidade")
plt.savefig("grafico1_barra_horizontal.png")
plt.close()

# ================================
# 2. GRÁFICO DE COLUNAS (vertical)
# Top produtos
# ================================
plt.figure(figsize=(12, 8))
plt.xticks(fontsize=8)
df.groupby("product")["total_items"].sum().nlargest(10).plot(kind="bar")
plt.title("Top 10 Produtos")
plt.savefig("grafico2_coluna_vertical.png")
plt.close()

# ================================
# 3. GRÁFICO DE LINHA
# Receita por mês (corrigido)
# ================================
plt.figure()
df['month'] = df['date'].dt.to_period('M').dt.to_timestamp()

df.groupby("month")["total_value"].sum().plot(kind="line")
plt.title("Receita por Mês")
plt.savefig("grafico3_linha.png")
plt.close()

# ================================
# 4. HISTOGRAMA
# Distribuição de preços
# ================================
plt.figure()
df['total_cost'].plot(kind='hist', bins=30)
plt.title("Distribuição de Preços")
plt.savefig("grafico4_histograma.png")
plt.close()

# ================================
# 5. GRÁFICO DE PIZZA
# Receita por cidade (Top 5)
# ================================
plt.figure()
df.groupby("city")["total_value"].sum().nlargest(5).plot(kind="pie", autopct='%1.1f%%')
plt.title("Top 5 Cidades por Receita")
plt.ylabel("")  # remove label feio
plt.savefig("grafico5_pizza.png")
plt.close()
