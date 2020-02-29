from db import nova_conexao

sql = 'select * from contatos where tel = "98765-4321"'

with nova_conexao() as conexao:
    cursor = conexao.cursor()
    cursor.execute(sql)

    for x in cursor:
        print(x)
    print(type(x))
