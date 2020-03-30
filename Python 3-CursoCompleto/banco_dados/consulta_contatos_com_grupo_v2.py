from collections import defaultdict
from db import nova_conexao
from mysql.connector.errors import ProgrammingError

sql = '''
    SELECT
        grupos.descricao AS Grupo,
        contatos.nome AS Nome
    FROM contatos
    INNER JOIN grupos ON contatos.grupo_id = grupos.id
    ORDER BY Grupo, Nome
'''

try:
    with nova_conexao() as conexao:
        try:
            cursor = conexao.cursor(dictionary=True)
            try:
                cursor.execute(sql)
                contatos = cursor.fetchall()
            finally:
                cursor.close()
        except ProgrammingError as e:
            print(f'Erro: {e.msg}')
        else:
            agrupados = defaultdict(list)
            for contato in contatos:
                agrupados[contato['Grupo']].append(contato['Nome'])
            print(agrupados)
            print(type(agrupados))
except ProgrammingError as e:
    print(f'Erro Externo: {e.msg}')
