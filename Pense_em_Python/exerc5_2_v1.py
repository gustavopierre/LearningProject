def check_fermat(a, b, c, n):
    if (n > 2 ) and (a ** n + b ** n == c ** n):
        print('Holy smokes, Fermat was wrong!')
    else:
        print('No, that doesn\'t work.')


n = int(input('Digite o valor de n? '))
a = int(input('Digite o valor de a? '))
b = int(input('Digite o valor de b? '))
c = int(input('Digite o valor de c? '))
check_fermat(a, b, c, n)