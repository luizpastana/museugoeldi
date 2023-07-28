# import pandas as pd
from flask import Flask
from sqlalchemy import create_engine, Table, MetaData, select
from collections import Counter

app = Flask(__name__)

engine = create_engine('sqlite:///bd_museu_goeldi.db')
metadata = MetaData()
table = Table('bd_museu_goeldi', metadata, autoload_with=engine)

with engine.connect() as connection:
    t = list()
    result = connection.execute(select(table))
    rows = [row for row in result]
    column = [column.name for column in table.columns]
    under_column = [s.replace(' ', '_') for s in column]
    for row in rows:
        t.append(dict(zip(under_column, row)))
    names = list()
    for especie in t:
        names.append(especie['Espécie'])
    under_names = [s.replace(' ', '_') for s in names]
    dict_names = dict(zip(under_names, t))


@app.route('/api/bd_museu_goeldi', methods=['GET'])
def get_names():
    return t[0]


@app.route('/api/bd_museu_goeldi/especies', methods=['GET'])
def get_especies():
    names = list()
    for especie in t:
        names.append(especie['Espécie'])
    return names


@app.route('/api/bd_museu_goeldi/bacias', methods=['GET'])
def get_bacias():
    bacias = list()
    for especie in t:
        bacias.append(especie['Bacia'])
    return Counter(bacias)


@app.route('/api/bd_museu_goeldi/extincao', methods=['GET'])
def get_extincao():
    extincao = list()
    for especie in t:
        extincao.append(especie['Categoria_de_risco_de_extinção_'])
    under_extincao = [s.replace(' ', '') for s in extincao]
    return Counter(under_extincao)


if __name__ == '__main__':
    app.run(debug=True)
