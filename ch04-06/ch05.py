# Big O só se preocupa com categorias no longo prazo. É uma notação que ignora constantes
# Dois algoritmos dentro de uma mesma categoria Big O podem ter quantidade de passos muito diferentes
# para o mesmo input
# Para diferenciar dois algoritmos dentro de uma mesma categoria precisamos, portanto
# de uma análise mais aprofundada

def print_even_numbers_till(upper_bound: int) -> None:
    number = 2

    while number <= upper_bound:
        if number % 2 == 0:
            print(number)
         
        number += 1
    
def print_even_faster(upper_bound: int) -> None:
    number = 2
    while number <= upper_bound:
        print(number)
        number += 2

# Ambos acima são O(N). A complexidade deles aumenta conforme N
# Porém, o segundo algoritmo é 2x mais rápido que o primeiro, apesar de estarem na msm categoria

# A mesma lógica poderia ser feita para Bubble Sort e Selection Sort, ambos O(N²)

# Perceba aqui que o primeiro seria:
# N comparações, N/2 prints, N increments -> O(2.5N) -> O(N) (ignoramos constantes)

# Q3: O algoritmo abaixo tem 2N passos, porém na notação Big O tem O(N) de complexidade
def double_then_sum(array:list)->int:
    doubled_array = []
    for i in array:
        doubled_array.append(i*2)

    total = 0
    for i in doubled_array:
        total += i
    
    return total

# Q4: O algoritmo abaixo é O(N), mesmo com 3 passos

def multiple_cases(array:list)->None:
    for string in array:
        print(string.upper())
        print(string.lower())
        print(string.capitalize())

# Q5: Se o índice de um número na array for par, retorna a soma do número com o tds os numeros
# da array
# A eficiência em Big O é O(N²), pois a quantidade de passos é simplesmente definida por
# (N / 2) * N = (N²/ 2) -> O(N²)
# Dividimos pela quantidade de índices pares e executamos N prints para cada índice par

def every_other(array:list)->None:
    for index, val in enumerate(array):
        if index % 2 == 0:
            for i in array:
                print(val + i)
