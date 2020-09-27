
valor1 = input('Ingrese el primer valor: ')
valor2 = input('Ingrese el segundo valor: ')
operacion = input('ingrese operacion a realizar :')

try:
    valor1 = int(valor1)
except:
    valor1 = 'no funciona'

if valor1 == 'no funciona':
    print('valor 1 no es un numero')
    exit()

try:
    valor2 = int(valor2)
except ValueError:
    valor2 = 'no funciona'

if valor2 == 'no funciona':
    print('valor 2 no es un numero')
    exit()

if operacion == '+':
    print('el valor de la suma es :', valor1 + valor2)

elif operacion == '-':
    print('el valor de la resta es:' , valor1 - valor2)

elif operacion == '*':
    print('el valor de la multiplicacion es :' , valor1 * valor2)

elif operacion == '/' and valor2 != 0:
    print('el valor de la division es :' , valor1 / valor2)
elif valor2 == 0:
    print('valor 2 debe ser distinto de cero')
else:
    print('no se ingreso una operacion valida')



