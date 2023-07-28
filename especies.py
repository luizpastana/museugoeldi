import pandas as pd
import sqlite3

# Ler o arquivo .xlsx em um DataFrame do pandas
df = pd.read_excel('Especies.xlsx')

# Criar uma conexão SQLite
conn = sqlite3.connect('bd_museu_goeldi.db')

df.to_sql('bd_museu_goeldi', conn, if_exists='replace', index=False)

# Escrever os dados do DataFrame para uma tabela SQLite
query = pd.read_sql_query("SELECT * FROM bd_museu_goeldi", conn)

t = list()
# rows = [row for row in query.values]
column = [column for column in query.columns]
t.append(dict(zip(column, query.values)))
# print(t)

# query2 = pd.read_sql_query("SELECT Bacia FROM bd_museu_goeldi", conn)

# Fechar a conexão
conn.close()

print(query)
