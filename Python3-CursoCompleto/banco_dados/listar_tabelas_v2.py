from db import nova_conexao
from mysql.connector.errors import ProgrammingError

try:
    with nova_conexao() as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute('show tables')
            for i, table in enumerate(cursor, start=1):
                print(f'Tabela {i}: {table[0]}')
        except ProgrammingError as e:
            print(f'Erro: {e.msg}')
except ProgrammingError as e:
    print(f'Erro Externo: {e.msg}')
