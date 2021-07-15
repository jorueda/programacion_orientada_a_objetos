# Prueba Codingame Koombea 2021.07.15

def codificar(cadena):

    contador = 0
    resultado = ""
    actual = cadena[0]
    for letra in cadena:

        if letra == actual:
            contador += 1
        else:
            resultado += str(contador) + actual
            contador = 1
            actual = letra

    resultado += str(contador) + actual
    return resultado

ingreso = input("Ingrese la cadena: ")
print(codificar(ingreso))
