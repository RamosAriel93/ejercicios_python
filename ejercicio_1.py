# edad = int(input('Ingrese su edad: '))
#
# if edad >= 18:
#     print("si puede ingresar")
# else:
#     print('fuera')

# dato = input('Ingrese dato: ')
#
# list = ['posho', 'luna', 'lola', 'posha']
#
# if list.count(dato) > 0:
#     print('El dato existe', dato)
# else:
#     print('El dato no existe')

# if dato in list:
#     print('El dato existe', dato)
# else:
#     print('El dato no existe')

valor1 = input('Ingrese el primer valor: ')
valor2 = input('Ingrese el segundo valor: ')
try:
    valor1 = int(valor1)
except:
    valor1 = 'no funciona'
try:
    valor2 = int(valor2)
except ValueError:
    valor2 = 'no funciona'
if valor1 == 'no funciona' or valor2 == 'no funciona':
    print('valores invalidos')
else:
    suma = valor1+valor2
    print('el resultado es :', suma)


