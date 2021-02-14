a = int(input('Ingrese el primer valor :'))
b = int(input('ingrese el segundo valor :'))
resultado = 0
for x in range(a):
    resultado += b
print('el resultado es :', resultado)


nombre = 'lola'
apellido = 'lula'
concadenacion = nombre + ' ' + apellido
print(concadenacion[::-1])

lista = [1, 2, 5, 6, 20, -15]
menor = 'init'
for x in lista:
    if menor == 'init':
        menor = x
    else:
        menor = x if x < menor else menor
print('numero menor :', menor)
