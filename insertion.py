#!/usr/bin/python3
import  random

def insertion_sort(array, size):

    for idx in range(size):
        value = array[idx]
        i = idx - 1
        while (i >= 0):
            if (value < array[i]):
                array[i], array[i + 1] = value, array[i]
                i = i - 1
            else:
                break
    return array


if __name__ == "__main__":
    size = int(input("Escribe el tamaño de la lista: "))

    array = [random.randint(0, 50) for _ in range(size)]
    print(array)
    new_array = insertion_sort(array, size)
    print(new_array)
