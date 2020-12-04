# -*- coding: utf-8 -*-

"""
Algoritmo de busqueda binaria recursiva escrito en Python
Este metodo funciona con cadenas y numeros por igual, ya
que el lenguaje trata a las cadenas lexicograficamente;
comparando sus valores en el codigo ASCII
"""


def binary_recursive_search(list_data, search_data, left_index, right_index):

    if left_index > right_index:
        return -1

    pivot_index = (left_index + right_index) // 2
    pivot_data = list_data[pivot_index]

    if pivot_data == search_data:
        return pivot_index
    if search_data < pivot_data:
        return binary_recursive_search(list_data, search_data, left_index, pivot_index - 1)
    else:
        return binary_recursive_search(list_data, search_data, pivot_index + 1, right_index)


"""
Tests:
"""

# Test con arreglo numericos
data_list = [1, 2, 3, 10, 50, 80, 120, 150, 500, 1000]

print("Busqueda para la lista: ", data_list)

data_search = 500

index_search = binary_recursive_search(data_list, data_search, 0, len(data_list) - 1)

print("El elemento {} esta en el indice {}".format(data_search, index_search))

# Test con arreglo de cadenas
data_list = ["Albino", "Bambu", "Becerro", "Contaminacion", "Cortina", "Trampolin"]

print("Busqueda para la lista: ", data_list)

data_search = "Cortina"

index_search = binary_recursive_search(data_list, data_search, 0, len(data_list) - 1)

print("El elemento {} esta en el indice {}".format(data_search, index_search))
