#!/usr/bin/python3
import random

def burbble_sort(array, size):
    for i in range(size):
        for j in range(size - i - 1):
            if array[j] > array[j + 1]:
                array[j] ,array[j + 1] = array[j + 1], array[j]
    return array


if __name__ == "__main__":
    size = int(input("Escribe el tamaño de la lista: "))

    array = [random.randint(0, 50) for _ in range(size)]
    print(array)
    new_list = burbble_sort(array, size)
    print(new_list)
