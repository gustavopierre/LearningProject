#!/usr/bin/python3
hora_inicial_seg = (6*60 + 25)*60
tempo = 2*(8*60+15)+3*(7*60+12)
hora_final_seg = hora_inicial_seg + tempo
hora = hora_final_seg//3600
min = (hora_final_seg % 3600)//60
seg = hora_final_seg-(hora*3600)-(min*60)
print(f'{hora}:{min:2d}:{seg:2d}')
