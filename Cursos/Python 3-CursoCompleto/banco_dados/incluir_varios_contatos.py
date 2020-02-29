from mysql.connector.errors import ProgrammingError
from db import nova_conexao

sql = 'insert into contatos (nome, tel) values (%s, %s)'
args = (
    ('Ana', '91234-5678'),
    ('Bia', '91234-5677'),
    ('Luca', '91234-5648'),
    ('Lu', '91234-5878'),
    ('Gui', '91234-5123'),
    ('Beca', '91456-5678'),
    ('Pedro', '99934-5678'),
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
            print(f'Foram incluídos {cursor.rowcount} registros.')
except ProgrammingError as e:
    print(f'Erro externo: {e.msg}')
