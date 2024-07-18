lista_cuentas = []
name = input('Ingrese su nombre: ')
last_name =input('Ingrese su apellido: ')
saldo = int(input('Ingrese su saldo:'))
lista_cuentas.append('Primera cuenta de ' + name)
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
print('Bienvenid@ ', name.upper(), last_name.upper(), sep=' ')
# print(name[-2])
# print('Caractares de apellido:')
# print(len(last_name))


#Operadores numericos
print('Estas son tus cuentas: ' ,lista_cuentas[:2])
x = 10
y = 5.6E4
print('Estos son tus saldos:',saldo, sep=' ')
print(type(lista_cuentas[0]))

# Creación de listas
lista_vacia = []
lista_numeros = [1, 2, 3, 4, 5]
lista_mixta = [1, "dos", 3.0, True]

config = {
    "host": "localhost",
    "port": 8080,
    "debug": True
}
print("Configuración:", config['port'])
def sum_values(values):
    result = []
    for i in range(len(values) - 1):
        sum = values[i] + values[i+1]
        result.append(sum)
    return result

values = [1, 2, 3, 4, 5]
result = sum_values(values)
print(result)

def calculadora():
    print("Bienvenido a la calculadora")
    print("Opciones:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    
    opcion = input("Seleccione una opción (1/2/3/4): ")
    
    if opcion in ['1', '2', '3', '4']:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        
        if opcion == '1':
            print(f"Resultado: {num1} + {num2} = {num1 + num2}")
        elif opcion == '2':
            print(f"Resultado: {num1} - {num2} = {num1 - num2}")
        elif opcion == '3':
            print(f"Resultado: {num1} * {num2} = {num1 * num2}")
        elif opcion == '4':
            if num2 != 0:
                print(f"Resultado: {num1} / {num2} = {num1 / num2}")
            else:
                print("Error: División por cero no permitida")
    else:
        print("Opción no válida")

# Llamada a la función calculadora para probarla
calculadora()

def fibonacci(n):
    if n < 0:
        print("Incorrecto, el valor debe ser positivo")
        return
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def calculator():
    opcion = input("Seleccione una opción (1/2): ")
    if opcion in ['1', '2']:
        num = int(input("Ingrese el número: "))
        if opcion == '1':
            print(f"El {num}er término de la secuencia Fibonacci es: {fibonacci(num)}")
            