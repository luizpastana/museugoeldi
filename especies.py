import pandas as pd
import sqlite3
from flask import Flask, jsonify
from sqlalchemy import create_engine, MetaData, Table, select

app = Flask(__name__)

# Ler o arquivo .xlsx em um DataFrame do pandas
df = pd.read_excel('Especies.xlsx')

# Criar uma conexão SQLite
# conn = sqlite3.connect('bd_museu_goeldi.db')
engine = create_engine('sqlite:///bd_museu_goeldi.db')

# df.to_sql('bd_museu_goeldi', engine, if_exists='replace', index=False)

metadata = MetaData()
table = Table('bd_museu_goeldi', metadata, autoload_with=engine)

@app.route('/api/bd_museu_goeldi', methods=['GET'])
def get_data():
    with engine.connect() as connection:
        result = connection.execute(select(table))
        rows = [list(row) for row in result]
    return rows

if __name__ == '__main__':
    app.run(debug=True)

#query = select(table).where(table.columns.Bacia == 'Xingu')
#with engine.connect() as connection:
 #   result = connection.execute(query)
  #  for row in result:
   #     print(row[1])
# Escrever os dados do DataFrame para uma tabela SQLite
# query = pd.read_sql_query("SELECT Espécie FROM bd_museu_goeldi", conn)

# Fechar a conexão
# conn.close()

#print(query)