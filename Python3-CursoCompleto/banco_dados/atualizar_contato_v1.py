from db import nova_conexao
from mysql.connector.errors import ProgrammingError

sql = 'update contatos set nome = %s where id = %s'
args = ('João', 22)

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql, args)
        conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print('Registro alterado.')
