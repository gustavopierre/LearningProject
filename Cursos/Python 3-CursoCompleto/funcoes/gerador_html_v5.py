#!/usr/bin/python3
bloco_atribs = ('bloco_accesskey', 'bloco_id')
ul_atribs = ('ul_id', 'ul_style')


def filtrar_atribs(informados, suportados):
    return ' '.join(f'{k.split("_")[-1]}="{v}"'
                    for k, v in informados.items() if k in suportados)


def tag_bloco(conteudo, *args, classe='success', inline=False, **novos_atrbs):
    tag = 'span' if inline else 'div'
    html = conteudo if not callable(conteudo) \
        else conteudo(*args, **novos_atrbs)
    atributos = filtrar_atribs(novos_atrbs, bloco_atribs)
    return f'<{tag} {atributos} class="{classe}">{html}</{tag}>'


def tag_lista(*itens, **novos_atrbs):
    lista = ''.join(f'<li>{item}</li>' for item in itens)  # generator
    return f'<ul {filtrar_atribs(novos_atrbs, ul_atribs)}>{lista}</ul>'


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
    print(tag_bloco(tag_lista, 'Item 1', 'Item 2', classe='info',
                    bloco_accesskey='m', bloco_id='conteudo', ul_id='lista'))
