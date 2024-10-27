"""
sumDigits
=========
Suma todos los dígitos de un número entero.

Principio de los vasos comunicantes.
 n! = i! * a
    = i * (i-1)! * a
    = (i-1)! * (i*a)
 We have: i'=i-1 and a'=i*a

Invariant programming en Python.
"""

def factorial(n):
    # Comprobación de seguridad en los datos de entrada
    if not isinstance(n, int):
        raise ValueError("El valor de entrada debe ser un número entero")
    if n < 0:
        raise ValueError("El valor de entrada debe ser un número entero no negativo")

    def factorialR(n, a):
        if n==0:
            return a
        else:
            return factorialR(n-1, n*a)
    return factorialR(n, 1)

def sumDigits(n):
    # Comprobación de seguridad en los datos de entrada
    if not isinstance(n, int):
        raise ValueError("El valor de entrada debe ser un número entero")
    if n < 0:
        raise ValueError("El valor de entrada debe ser un número entero no negativo")

    def sumDigitsR(n, a):
        if n == 0:
            return a
        else:
            return sumDigitsR(n // 10, a + n % 10)

    return sumDigitsR(n, 0)

# Pruebas
print(f"The factorial of 14 is {factorial(14)}")

try:
    print(sumDigits(12345))  # Salida esperada: 15
    #print(sumDigits(-12345)) # Debería lanzar una excepción
    print(sumDigits("12345")) # Debería lanzar una excepción
except ValueError as e:
    print(e)




