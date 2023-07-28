import pandas as pd
import sqlite3

# Ler o arquivo .xlsx em um DataFrame do pandas
df = pd.read_excel('Especies.xlsx')

# Criar uma conexão SQLite
conn = sqlite3.connect('bd-museu-goeldi.db')

# Escrever os dados do DataFrame para uma tabela SQLite
df.to_sql('especies', conn, if_exists='replace', index=False)

# Fechar a conexão
conn.close()

print(df)