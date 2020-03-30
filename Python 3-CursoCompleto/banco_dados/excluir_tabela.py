from db import nova_conexao
from mysql.connector.errors import ProgrammingError

exclui_tabela_email = """
    drop table if exists emails
"""
exclui_tabela_grupos = """
    drop table if exists grupos
"""

try:
    with nova_conexao() as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(exclui_tabela_email)
            cursor.execute(exclui_tabela_grupos)
        except ProgrammingError as e:
            print(f'Erro: {e.msg}')
except ProgrammingError as e:
    print(f'Erro externo: {e.msg}')
