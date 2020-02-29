from mysql.connector import connect

conexao = connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='12345678',
    database='agenda'
)

cursor = conexao.cursor()
cursor.execute('show tables')

for i, table in enumerate(cursor, start=1):
    print(f'Tabela {i}: {table[0]}')
