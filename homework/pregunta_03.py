"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv

def pregunta_03():
    suma_por_letra = {}
    with open('files/input/data.csv', newline='') as f:
        reader = csv.reader(f, delimiter='\t')
        for row in reader:
            letra = row[0]
            valor = int(row[1])
            suma_por_letra[letra] = suma_por_letra.get(letra, 0) + valor
    letras = sorted(suma_por_letra.items())
    return letras
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
print(pregunta_03())