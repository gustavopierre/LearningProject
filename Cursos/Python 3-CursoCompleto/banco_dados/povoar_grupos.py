from db import nova_conexao
from mysql.connector.errors import ProgrammingError

sql = 'INSERT INTO grupos (descricao) VALUES (%s)'
args = (
    ('casa',),
    ('trabalho',),
)

try:
    with nova_conexao() as conexao:
        try:
            cursor = conexao.cursor()
            cursor.executemany(sql, args)
            conexao.commit()
        except ProgrammingError as e:
            print(f'Erro: {e.msg}')
        else:
            print(f'{cursor.rowcount} registros inseridos.')
except ProgrammingError as e:
    print(f'Erro Externo: {e.msg}')
