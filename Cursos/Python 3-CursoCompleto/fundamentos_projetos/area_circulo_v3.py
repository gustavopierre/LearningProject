from math  import pi

def circulo(raio):
    area = pi*(float(raio)**2)
    print(area)

if  __name__ == '__main__':
    raio = input('Informe o raio: ')
    circulo(raio)
    
