from time import time

def factorial(n):
    respuesta = 1

    while n > 1:
        respuesta *= n
        n -= 1

    return respuesta

def factorial_recursivo(n):
    if n == 1:
        return 1

    return n * factorial_recursivo(n-1)


if __name__ == '__main__':
    n = 998

    comienzo = time()
    factorial(n)
    final = time()
    print(f'El tiempo del factorial normal es: {(final - comienzo)*1000}ms')

    comienzo = time()
    factorial_recursivo(n)
    final = time()
    print(f'El tiempo del factorial recursivo es: {(final - comienzo)*1000}ms')
