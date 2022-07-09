from math import floor, log2

# Q1: Em Big O, o algoritmo abaixo tem complexidade O(1). 

def isLeapYear(year: int) -> bool:
    return (year % 400 == 0) if (year % 100 == 0)  else (year % 4 == 0)


# Q2: O algoritmo abaixo tem complexidade O(N). Ele vai acumulando em cada passo
# e a quantidade de passos aumenta conforme o tamanho da array
def arraySum(array: list) -> float:
    sum = 0

    for i in range(len(array)):
        sum += array[i]
    
    return sum

# Q3: O algoritmo abaixo tem complexidade O( log N), pois a cada vez que o loop itera
# o valor de placedgrains dobra. Ou seja, para cada dobro do input, o algoritmo só executa um passo a mais

def chessboard_space(number_of_grains: int) -> int:
    chessboard_spaces = 1
    placed_grains = 1

    while (placed_grains < number_of_grains):
        placed_grains *= 2
        chessboard_spaces += 1;
    return chessboard_spaces

# Q4: O algoritmo abaixo tem complexidade O(N). Ele tem que verificar até o final
# da lista se a string começa com "a"

def select_a_strings(array: list) -> list:
    new_array = []

    for i in array:
        if i.startswith("a"):
            new_array.append(i)
    
    return new_array

# Q5: A função calcula a mediana de uma ordered array/lista ordenada
# Sua complexidade é O(1) **para ordered arrays**

def median(array:list)->float:
    middle = floor(len(array) / 2)

    if (len(array) % 2 == 0):
        return (array[middle - 1] + array[middle + 1]) / 2
    else:
        return array[middle]