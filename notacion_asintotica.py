
def fibonacci(n):

    if n == 0:
        return 0
    elif n == 1:
        return 1

    return fibonacci(n-1) + fibonacci(n-2)

if __name__ == '__main__':
    n = int(input("Elija un número entero para calcular Fibonacci: "))

    print(fibonacci(n))
