# Estratégia geral para otimização algorítimica:
#  - Determinar a eficiência atual
#  - Imaginar se há espaço pra otimização
#  - Aplicar alguma das técnicas de otimização:
#       -> Programação Dinâmica (Memoização, recursão em calda)
#       -> Aplicar uma hash table para caso seja necessário fazer lookups em O(1) 
#       -> Observar padrões gerais do problema (Exemplos e casos)
#       -> Algoritmos gulosos
#       -> Mudar a estrutura de dados envolvida no problema

# Algoritmos gulosos/greedy: Algoritmos que, em cada passo, escolhem aquela que parece ser a melhor opção naquele dado momento
# Exemplo: encontrar o maior valor numa array
def greedy_max(array:list):
    # Como é greedy, no começo a melhor decisão parece ser que o maior valor da array seja o primeiro, o único que o algoritmo "encontrou" até agora
    greatest_val = array[0]
    for i in array[1:]:
        if i > greatest_val: # Caso encontre um maior, a melhor decisão nesse momento é mudar o valor de greatest_val
            greatest_val = i
    
    # Após N interações, retornamos o maior valor
    return greatest_val

# Exemplo: Encontrar a maior soma de uma sub-array
# a chave é perceber o padrão que caso a soma corrente seja menor que 0, faz sentido "resetar" a soma
def greedy_greatest_subsum(array:list)->int:
    current_sum = 0
    greatest_sum = 0

    for num in array:
        if current_sum + num < 0:
            current_sum = 0
        else:
            current_sum += num
        
        if (current_sum > greatest_sum):
            greatest_sum = current_sum
    
    return greatest_sum

# EXERCICIOS
# Q1: Ir de O(N*M) para O(N + M) prum algoritmo que recebe duas arrays com nomes e modalidade de vários atletas e achar a intersecção dessas duas arrays
# Ou seja, encontrar jogador que jogam ambos os esportes
basketball_players = [
{'first_name': "Jill", 'last_name': "Huang", 'team': "Gators"},
{'first_name': "Janko", 'last_name': "Barton", 'team': "Sharks"},
{'first_name': "Wanda", 'last_name': "Vakulskas", 'team': "Sharks"},
{'first_name': "Jill", 'last_name': "Moloney", 'team': "Gators"},
{'first_name': "Luuk", 'last_name': "Watkins", 'team': "Gators"}
]

football_players = [
{'first_name': "Hanzla", 'last_name': "Radosti", 'team': "32ers"},
{'first_name': "Tina", 'last_name': "Watkins", 'team': "Barleycorns"},
{'first_name': "Alex", 'last_name': "Patel", 'team': "32ers"},
{'first_name': "Jill", 'last_name': "Huang", 'team': "Barleycorns"},
{'first_name': "Wanda", 'last_name': "Vakulskas", 'team': "Barleycorns"}
]

def play_both_sports(arr1: list, arr2:list)->list:
    # hash_table para armazenar os valores da primeira arr
    arr1_athletes_hash_table = {}
    # lista para guardar os jogadores que estão presentes em ambos
    intersection_list = []

    for player in arr1:
        full_name = player['first_name'] + ' ' + player['last_name']
        # armazena cada jogador na arr1
        arr1_athletes_hash_table[full_name] = True
    
    for player in arr2:
        full_name = player['first_name'] + ' ' + player['last_name']
        # se esse mesmo jogador estiver presente na arr2, adicione na lista de intersecção
        if arr1_athletes_hash_table.get(full_name):
            intersection_list.append(full_name)
    
    return intersection_list

# Complexidade de tempo: O(N + M)
# Complexidade espacial: O(N) (depende do tamanho da primeira array)

# Q2: Dada um array L, uma sequência de a até b, porém faltando um número c, retornar c
# Obs: a, b e c todos naturais
# Deve ser O(N):
def missing_number_from_sequence(arr:list)->int:
    # Uma abordagem bem greedy. Assumimos que o primeiro numero mais um é o número q está faltando,
    # pois o algoritmo ainda não encontrou esse numero
    missing_number = arr[0] + 1
    for num in arr[1:]:
        # se o numero atual não for igual a esse missing number (ou seja, não for o sucessor do anterior), retorna ele
        if not (num == missing_number):
            return missing_number
        missing_number += 1
# Complexidade de tempo: O(N)
# Complexidade de espaço: O(1)

# Q3: Fazer função O(N) que retorne o maior lucro dado uma única ação de buy seguida por uma única ação de sell
example_stocks = [10, 7, 5, 8, 11, 2, 6]

# Outra abordagem greedy
def greatest_profit(arr:list)->int:
    # o primeiro valor que compramos será o primeiro da array
    buy_init_val = arr[0]
    # o maior lucro até agora é zero. Ainda não "vendemos" a nossa ação
    greatest_profit_so_far = 0

    for price in arr[1:]:
        # caso o preço da ação seja menor que o preço da ação que compramos anteriomente, "resetamos" o algoritmo
        if price < buy_init_val:
            buy_init_val = price
            greatest_profit_so_far = 0
        # caso contrario (o preço seja igual, ou maior que o preço da ultima ação comprada), aumentamos o preço que esperamos vender a ação no final
        else:
            greatest_profit_so_far += price
        
    return greatest_profit_so_far

# Complexidade de tempo: O(N)
# Complexidade de espaço: O(1)

# Q4: Designar um algoritmo que aceita uma lista L e retorna os dois números de L que,
# multiplicados entre si, retornam o maior produto possível entre dois números 
# distintos de L
def greatest_product(arr:list)->list:
    # Todos os números serão maiores que -inf
    greatest_number = -float('inf')
    second_greatest_number = -float('inf')

    # Todos os números serão maiores que +inf
    smallest_number = float('inf')
    second_smallest_number = float('inf')

    for i in arr:
        if i >= greatest_number:
            second_greatest_number = greatest_number
            greatest_number = i
        elif i >= second_greatest_number:
            second_greatest_number = i

        if i <= smallest_number:
            second_smallest_number = smallest_number
            smallest_number = i
        elif i <= second_smallest_number:
            second_smallest_number = i

    greatest_product_positive = greatest_number * second_greatest_number
    greatest_product_negative = smallest_number * second_smallest_number

    return max(greatest_product_positive, greatest_product_negative)

# Complexidade de tempo: O(N)
# Complexidade de espaço: O(1)

# Q5: Dada uma array de amostras de temperaturas que tem um limite inferior igual a 
# 97 graus F e superior igual a 99 graus F, ordenar a array em O(N)

def sort_temps(arr: list[float])->list[float]:
    # Criamos uma hash table que irá armazenar as ocorrências de temperatura
    hash_temps :dict[float, int] = {}

    for temp in arr:
        if hash_temps.get(temp):
            hash_temps[temp] += 1
        else:
            hash_temps[temp] = 1
    
    sorted_arr :list[float]= []
    temperature :int = 970
    while temperature <= 990:
        if hash_temps.get(temperature / 10):
            for i in range(hash_temps[temperature]):
                sorted_arr.append(temperature/10)
        
        temperature += 1
    
    return sorted_arr

# Complexidade de tempo: O(N)    
# Complexidade de espaço: O(N), pois criamos uma hash table e uma array com N elementos cada


# Q6: Uma função que retorna o tamanho da maior sub-sequência consecutiva
# de uma lista de inteiros L, em tempo O(N)
# Ex: [10, 5, 12, 3, 55, 30, 4, 11, 2] 
# => maior sub-sequência consecutiva = [2, 3, 4, 5]
# => tamanho da maior sub-sequencia consecutiva = 4

def size_greatest_consec_subseq(arr: list[int]) -> int:
    occurences :dict[int, bool] = {}
    greatest_len :int = 0

    for i in arr:
        occurences[i] = True
    
    for i in arr:
        if not occurences.get(i - 1):
            current_len :int = 1
            current_num :int = i

            while occurences.get(current_num + 1):
                current_num += 1
                current_len += 1

                if current_len > greatest_len:
                    greatest_len = current_len
    
    return greatest_len

# Complexidade de tempo: O(N)
# Complexidade de espaço: O(N)
