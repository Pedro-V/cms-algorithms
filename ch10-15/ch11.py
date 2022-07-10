# Staircase problem
def number_of_paths(n):
    if n < 0:
        return 0
    elif n == 1 or n == 0:
        return 1
    else:
        return number_of_paths(n - 1) + number_of_paths(n - 2) + number_of_paths(n - 3)

# Q1: Contar caracteres numa lista de strings

def count_chars(words:list)-> int:
    if len(words) == 0:
        return 0
    return len(words[0]) + count_chars(words[1:])

# Q2: Recebe uma array de números e retorna uma array apenas com números pares
def filter_even(arr:list)-> list:
    if arr == []:
        return []
    return ([arr[0]] if arr[0] % 2 == 0 else []) + filter_even(arr[1:])

# Q3: Função recursive para calcular os números triangulares
def triangular_numbers(N:int)-> int:
    if N == 1:
        return N
    return N + triangular_numbers(N - 1)

# Q4: Retorna o primeiro índice que contém "x". Assume-se que a string contém pelo menos um "x"
def first_x_index(word:str)->int:
    if word[0] == "x":
        return 0
    return 1 + first_x_index(word[1:])

# Q5: Escrever uma função para calcular a quantidade de caminhos mais curtos possíveis
# no problema de "Unique Paths"
# R  C    P
# 1  1 =  0
# 1  2 =  1
# 2  1 =  1
# 2  2 =  2
# 1  3 =  2
# 2  3 =  3

# Talvez as condições não tenham que ser tão hardcoded assim
def num_short_paths(rows:int, columns:int)->int:
    if rows == 1 or columns == 1:
        return 1
    return num_short_paths(rows - 1, columns) + num_short_paths(rows, columns - 1)

# Essa função não é eficiente. Podemos fazer uso de memoization pra aumentar a eficiência:

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