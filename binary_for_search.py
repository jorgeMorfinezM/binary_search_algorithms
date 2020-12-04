# -*- coding: utf-8 -*-

"""
Algoritmo de busqueda binaria usando el ciclo while
escrito en Python.

Este metodo funciona con cadenas y numeros por igual, ya
que el lenguaje trata a las cadenas lexicograficamente;
comparando sus valores en el codigo ASCII
"""


def binary_search(list_data, search_data):
    left_index, right_index = 0, len(list_data) - 1
    while left_index <= right_index:
        pivot_index = (left_index + right_index) // 2

        pivot_data = list_data[pivot_index]

        if pivot_data == search_data:
            return pivot_index
        if search_data < pivot_data:
            right_index = pivot_index - 1
        else:
            left_index = pivot_index + 1

    # sale del ciclo, significa que no existe el valor buscado en el arreglo
    return -1


"""
Tests
"""

# Test con arreglo numericos
data_list = [1, 2, 3, 10, 50, 80, 120, 150, 500, 1000]

print("Busqueda para la lista: ", data_list)

data_search = 500

index_search = binary_search(data_list, data_search)

print("El elemento {} esta en el indice {}".format(data_search, index_search))

# Test con arreglo de cadenas
data_list = ["Albino", "Bambu", "Becerro", "Contaminacion", "Cortina", "Trampolin"]

print("Busqueda para la lista: ", data_list)

data_search = "Cortina"

index_search = binary_search(data_list, data_search)

print("El elemento {} esta en el indice {}".format(data_search, index_search))