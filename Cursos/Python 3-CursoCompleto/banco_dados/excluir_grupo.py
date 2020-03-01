from db import nova_conexao
from mysql.connector.errors import ProgrammingError

sql = 'delete from grupos where descricao = %s'
args = (
    ('casa',),
    ('trabalho',)
)
with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.executemany(sql, args)
        conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print(f'{cursor.rowcount} registros deletados.')
