#!/usr/bin/python3
def tag_bloco(conteudo, *args, classe='success', inline=False):
    tag = 'span' if inline else 'div'
    html = conteudo if not callable(conteudo) else conteudo(*args)
    return f'<{tag} class="{classe}">{html}</{tag}>'


def tag_lista(*itens):
    lista = ''.join(f'<li>{item}</li>' for item in itens)  # generator
    return f'<ul>{lista}</ul>'


if __name__ == '__main__':
    print(tag_bloco('bloco'))
    '''
        aqui ele considera todos os argumentos
        como elementos do parametro packing
    '''
    print(tag_bloco('inline e classe', 'info', True))
    print(tag_bloco('inline', inline=True))
    print(tag_bloco('falhou', classe='error'))
    print(tag_bloco('falhou', 'error'))
    print(tag_bloco(inline=True, conteudo='Falhou!!!', classe='error'))
    print(tag_bloco(tag_lista('Item 1', 'Item 2'), 'info'))
    # os parâmetros depois de um packing têm que ser
    # nomeados, não podem ser posicionais
    print(tag_bloco(tag_lista, 'Sábado', 'Domingo',
                    classe='info', inline=True))
