from itertools import product
from typing import Any


def leer_matriz(cadena):
    matriz = []
    filas = cadena.strip().split(';')
    for fila in filas:
        if fila.strip()== "":
            continue

        numeros_str = fila.strip().split()
        fila_numeros = []
        for n in numeros_str:
            fila_numeros.append(int(n))
        matriz.append(fila_numeros)
    if not matriz:
        raise ValueError("La matriz no puede estar vacía")

    ancho = len(matriz[0])
    for fila in matriz:
        if len(fila) != ancho:
            raise ValueError("Todas las filas deben de tener el mismo numero de columnas")

    return matriz

def suma_matrices(ma,na):
    if len(ma)!=len(na) or len(ma[0]) != len(na[0]):
        raise ValueError("Las matrices deben tener el mismo tamaño ")
    resultado = []
    for i in range(len(ma)):
        fila_resultado = []
        for j in range(len(ma[0])):
            fila_resultado.append(ma[i][j]+na[i][j])
        resultado.append(fila_resultado)
    return resultado

def resta_matrices(ma,na):
    if len(ma)!=len(na) or len(ma[0]) != len(na[0]):
        raise ValueError("Las matrices deben tener el mismo tamaño ")
    resultado = []
    for i in range(len(ma)):
        fila_resultado = []
        for j in range(len(ma[0])):
            fila_resultado.append(ma[i][j] - na[i][j])
        resultado.append(fila_resultado)
    return resultado


def imprimir_matriz(matriz):
    for fila in matriz:
        print(" ".join(f"{num:>4}" for num in fila))
    print()

def multiplica_matrices(ma,na):
    if len(ma[0])!=len(na):
        raise ValueError("Número de columnas de la primera matriz debe ser igual al número de filas de la segunda")
    resultado = []
    for i in range(len(ma)):
        fila_resultado= []
        for j in range(len(na[0])):
            suma = 0
            for k in range(len(ma[0])):
                suma += ma[i][k]*na[k][j]
            fila_resultado.append(suma)
        resultado.append(fila_resultado)
    return resultado

def pedir_matrices():
    entrada1 = input("Introduce la matriz 1 (filas separadas por ';'): ")
    entrada2 = input("Introduce la matriz 2 (filas separadas por ';'): ")
    return leer_matriz(entrada1), leer_matriz(entrada2)

def pedir_matriz():
    entrada1 = input("Introduce la matriz (filas separadas por ';'): ")
    return leer_matriz(entrada1)

def traspuesta_matriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    resultado = []
    for j in range(columnas):
        fila_resultado = []
        for k in range(filas):
            fila_resultado.append(matriz[k][j])
        resultado.append(fila_resultado)
    return resultado

def determinante(matriz):
    n = len(matriz)
    for fila in matriz:
        if len(fila) != n:
            raise ValueError("La matriz debe ser cuadrada para calcular el determinante")
    if n == 2:
        return matriz[0][0]*matriz[1][1] - matriz[0][1]*matriz[1][0]

    det = 0
    for j in range(n):
        submatriz = [fila[:j] + fila[j+1:] for fila in matriz[1:]]
        det += (-1)**j * matriz[0][j] * determinante(submatriz)
    return det


def main():
    print("******** Calculadora de Matrices ver 1.0 ********")
    while True:
        accion = input("Ingresa una opción: suma(+), resta(-), multiplicacion(*), traspuesta(t), determinante (Det) o exit: ").strip().lower()
        match accion:
            case '+':
                m, n = pedir_matrices()
                resultado = suma_matrices(m, n)
                imprimir_matriz(resultado)
            case '-':
                m, n = pedir_matrices()
                resultado = resta_matrices(m, n)
                imprimir_matriz(resultado)
            case '*':
                m, n = pedir_matrices()
                resultado = multiplica_matrices(m, n)
                imprimir_matriz(resultado)
            case 't':
                m = pedir_matriz()
                resultado = traspuesta_matriz(m)
                imprimir_matriz(resultado)
            case 'det':
                m = pedir_matriz()
                resultado = determinante(m)
                print(resultado)
            case 'exit':
                print("¡Hasta luego!")
                break
            case _:
                print("Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    main()
