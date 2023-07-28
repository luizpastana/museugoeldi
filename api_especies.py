import pandas as pd
from flask import Flask, jsonify
from sqlalchemy import create_engine, Table, MetaData, select, insert

app = Flask(__name__)

engine = create_engine('sqlite:///bd_museu_goeldi.db')
metadata = MetaData()
table = Table('bd_museu_goeldi', metadata, autoload_with=engine)

df = pd.read_excel('Especies.xlsx')

# Crie a consulta de inserção
insert(table).values(df)

@app.route('/api/bd_museu_goeldi', methods=['GET'])
def get_data():
    with engine.connect() as connection:
        result = connection.execute(select(table))
        rows = [list(row) for row in result]
        column = [column.name for column in table.columns]
    return rows

if __name__ == '__main__':
    app.run(debug=True)
