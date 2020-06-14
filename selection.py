#!/usr/bin/python3
import random


def selection_sort(array, size):

    for i in range(size - 1):
        min_num = i
        for j in range(i + 1, size):
            if array[j] < array[min_num]:
                min_num = j
        if array[i] > array[min_num]:
            array[i], array[min_num] = array[min_num], array[i]

    return array


if __name__ == "__main__":
    size = int(input("Escribe el tamaño de la lista: "))

    array = [random.randint(0, 50) for _ in range(size)]
    print(array)
    new_array = selection_sort(array, size)
    print(new_array)
