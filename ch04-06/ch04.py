import random
from timeit import timeit


def bubble_sort(ls:list) -> list:
    unsorted_until_index = len(ls) - 1
    is_sorted = False

    while not is_sorted:
        is_sorted = True
        for i in range(unsorted_until_index):
            if ls[i] > ls [i+1]:
                ls[i], ls[i+1] = ls[i+1], ls[i]
                is_sorted = False
        unsorted_until_index -= 1
    
    return ls
# O worst case desse algoritmo de ordenação seria uma ls em ordem decrescente

# Perceba a ineficiencia:
#    N (tamanho ls)   # Num max de passos (worst case)
#           5                   20
#          10                   90
#          20                  380
#          40                 1560
#          80                 6320

# O(N^2) é a complexidade desse algoritmo

def make_random_size_list(N: int) -> list:
    randomlist = []

    for i in range(N):
        randomlist.append(random.randint(0, 100))
    
    return randomlist

bubble_sort([1, 2, 4, 1])    

pequena = make_random_size_list(100)
media = make_random_size_list(1000)
grande = make_random_size_list(10000)

def has_duplicate_value(array:list) -> bool:
    existingNumbers = []

    for i in array:
        if i in existingNumbers:
            return True
        existingNumbers.append(i)
    
    return False

# O algoritmo abaixo tem complexidade O(N^2)
def greatest_number(array):
    for i in array:
        isIValTheGreatest = True

        for j in array:
            if j > i:
                isIValTheGreatest = False

        if isIValTheGreatest:
            return i

# Reescrevendo o algoritmo para ter eficiencia O(N):

def linear_greatest_number(array:list) -> int:
    maior = array[0]
    for i in array[1:]:
        if i > maior:
            maior = i
    
    return maior

setup="from __main__ import greatest_number, linear_greatest_number, grande"

timeit(setup=setup, stmt="greatest_number(grande)", number=10000)
timeit(setup=setup, stmt="linear_greatest_number(grande)", number=10000)
