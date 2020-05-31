from db import nova_conexao
from mysql.connector import ProgrammingError
tabela_contatos = """
    create table if not exists contatos(nome varchar(50), tel varchar(40))
"""

tabela_emails = """
    create table if not exists emails(
        id int auto_increment primary key,
        dono varchar(50)
    )
"""
try:
    with nova_conexao() as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(tabela_contatos)
            cursor.execute(tabela_emails)
        except ProgrammingError as e:
            print(f'Erro: {e.msg}')
except ProgrammingError as e:
    print(f'Erro CONEXÃO: {e.msg}')
