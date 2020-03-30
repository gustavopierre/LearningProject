from mysql.connector import connect
from mysql.connector.errors import ProgrammingError

conexao = connect(
    host='localhost',
    database='agenda',
    user='root',
    passwd='12345678',
    port=3306
)

sql = 'update contatos set nome = %s where id = %s'
args = ('Beatriz', 23)

try:
    cursor = conexao.cursor()
    cursor.execute(sql, args)
    conexao.commit()
except ProgrammingError as e:
    print(f'Erro: {e.msg}')
else:
    print('Registro alterado.')
