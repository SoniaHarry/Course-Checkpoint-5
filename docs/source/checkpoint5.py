#1.Cree un bucle For de Python.
for i in range(1,6):
    print(i) #1,2,3,4,5

#2.Cree una función de Python llamada suma que tome 3 argumentos y devuelva la suma de los 3.
def suma (num1,num2,num3):
    return num1+num2+num3


print (f'Resultado:{suma (2,3,4)}')

#3.Cree una función lambda con la misma funcionalidad que la función de suma que acaba de crear.
result= lambda num1, num2, num3: num1+num2+num3
print(f'Resultado lambda:{result(2,3,4)}')

#4.Utilizando la siguiente lista y variable, determine si el valor de la variable coincide o no con un valor de la lista. 
#*Sugerencia, si es necesario, utilice un bucle for in y el operador in.
nombre = 'Enrique'
lista_nombre = 'Jessica', 'Paul', 'George', 'Henry', 'Adán'

#Una forma de hacerlo
if (nombre in lista_nombre):
    print (f"{nombre} Existe en la lista {lista_nombre}")
else:
    print(f"{nombre} No existe en la lista {lista_nombre}")

#Otra forma de hacerlo con bucle for 
def existe ( nombre, lista_nombres):
    for elemento in lista_nombres:
        if nombre == elemento: return True
        

if existe(nombre, lista_nombre):
    print (f"{nombre} Existe en la lista {lista_nombre}")
else:
    print(f"{nombre} No existe en la lista {lista_nombre}")




