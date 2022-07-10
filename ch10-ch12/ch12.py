def max_num_arr(arr:list)->int:
    first = arr[0]
    if len(arr) == 1:
        return first
    
    max_rest = max_num_arr(arr[1:])
    return max_rest if max_rest > first else first

# Q1: Soma números de uma lista. Se essa soma ultrapassar 100, ignore todos os números seguintes:

# Essa função funciona particularmente de trás pra frente
# Por ex: add_until_100([10, 90, 1]) vai retornar 91 (90 + 1, ignora o 10)
# O comportamento esperado de add_until_100([10, 90, 1]) = 100 (10 + 90, ignora o um) pode ser obtido
# adicionando a função de reverse na add_until_100, ou modificando alguns detalhes na nova add_until_100_rev
def add_until_100(array:list)->int:
    # Caso base
    if len(array) == 0:
        return 0
    resto = add_until_100(array[1:])

    return resto if (array[0] + resto) > 100 else array[0] + resto

def add_until_100_rev(array:list)->int:
    # Caso base
    if len(array) == 0:
        return 0
    resto = add_until_100_rev(array[:-1])

    return resto if (array[-1] + resto) > 100 else array[-1] + resto


# Q2: Sequência de Golomb eficiente usando memoization
# Essa é a função ineficiente:
def ineff_golomb(n):
    if n == 1:
        return 1
    return 1 + ineff_golomb(n - ineff_golomb(ineff_golomb(n - 1)))

# Implementação da memoizada
def golomb_mem(n:int, memo:dict)->int:
    if n == 1:
        return 1
    
    if n not in memo:
        inner = golomb_mem(n - 1, memo)
        mid  = golomb_mem(inner, memo)
        increment = golomb_mem(n - mid, memo)
        memo[n] = 1 + increment
    
    return memo[n]

# Simplificada
def golomb(n:int)-> int:
    return golomb_mem(n, {})

# Q3 solução memoizada que ja foi implementada no ch11.py

def memoized_short_paths(rows:int, cols:int, memo: dict):
    # caso base
    grid_size = (rows, cols)
    if rows == 1 or cols == 1:
        return 1
    
    if grid_size not in memo:
        memo[grid_size] = memoized_short_paths(rows - 1, cols, memo) + memoized_short_paths(rows, cols - 1, memo)

    return memo[grid_size]

# Principal: É extremamente eficiente mesmo para grids mtt grandes, como 100x100, 600x300, etc
def sum_short_paths(rows:int, cols:int):
    return memoized_short_paths(rows, cols, {})