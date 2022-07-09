# Q1: Intersecção de duas arrays, usando hash tables/dictionaries, com complexidade
# O(N):

def contains(key:int, hash_table:dict)->bool:
    try:
        hash_table[key]
    except:
        return False
    else:
        return True

def intersection(arr1: list, arr2: list)->list:
    larger_arr = max(arr1, arr2)
    smaller_arr = min(arr1, arr2)
    hash_t = dict()

    for i in larger_arr:
        hash_t[i] = True

    intersect_list = []

    for j in smaller_arr:
        if contains(j, hash_t):
            intersect_list.append(j)
    
    return intersect_list

# Q2: Uma função O(N) que retorna a primeira duplicata numa array de strings:
# Assume-se que existe pelo menos uma duplicata

def first_duplicate(arr:list)->str:
    steps = 0
    for i in range(len(arr)):
        elem_list = list(arr[i])
        steps += 1
        if intersection(elem_list, arr[i+1: ]):
            return arr[i], steps

# Q3 Uma função O(N) que receba uma string com todas as letras do alfabeto menos uma
# e retorna a faltante

def missing_letter(word:str)->str:
    word = word.lower()
    alphabet = list(range(97, 123))


    for w in alphabet:
        if chr(w) not in word:
            return chr(w)

# Q4 retorna a primeira não-duplicata, deve ser O(N)
# ex: "minimum" -> "n"

def first_non_dup(word:str)->str:
    container = dict()

    for w in word:
        if contains(w, container):
            container[w] += 1
        else: 
            container[w] = 1
    
    for letter in word:
        if container[letter] == 1:
            return letter
