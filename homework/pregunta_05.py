"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv

def pregunta_05():
    valores = {}
    with open('files/input/data.csv', newline='') as f:
        reader = csv.reader(f, delimiter='\t')
        for row in reader:
            letra = row[0]
            valor = int(row[1])
            if letra not in valores:
                valores[letra] = [valor, valor]  # [max, min]
            else:
                valores[letra][0] = max(valores[letra][0], valor)
                valores[letra][1] = min(valores[letra][1], valor)
    resultado = sorted([(letra, v[0], v[1]) for letra, v in valores.items()])
    return resultado

print(pregunta_05())

"""
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]
"""