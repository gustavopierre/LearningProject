from mysql.connector.errors import ProgrammingError
from db import nova_conexao

sql = 'select * from contatos limit %s offset %s'
# args = (10, 10)
try:
    with nova_conexao() as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(sql, (10, 10))
            # cursor.execute(sql, args)
            contatos = cursor.fetchall()
        except ProgrammingError as e:
            print(f'Erro: {e.msg}')
        else:
            for contato in contatos:
                print(
                    f'{contato[2]:2d} - {contato[0]:15s} Telefone:{contato[1]}'
                )
except ProgrammingError as e:
    print(f'Erro externo: {e.msg}')
