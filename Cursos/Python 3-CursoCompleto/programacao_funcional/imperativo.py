#!/usr/bin/python3
from locale import setlocale, LC_ALL
from calendar import mdays, month_name

# Portugues do Brasil
setlocale(LC_ALL, 'pt_BR.utf8')

print('Meses com 31 dias:')
for mes in range(1, 13):
    if mdays[mes] == 31:
        print(f'- {month_name[mes]}')
