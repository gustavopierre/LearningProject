from db import nova_conexao

# sql = 'select * from contatos order by nome desc'
# ascendente não precisa especificar, pois é o default
sql = 'select * from contatos order by nome'

with nova_conexao() as conexao:
    cursor = conexao.cursor()
    cursor.execute(sql)

    # print('\n'.join(registro[0] for registro in cursor))
    print('\n'.join(str(registro) for registro in cursor))
    # print('\n'.join(str(registro[1]) for registro in cursor))
