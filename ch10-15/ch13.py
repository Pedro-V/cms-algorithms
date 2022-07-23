# Implementando uma classe com método de partição simples
from random import randint


class SortableArray:
    def __init__(self, arr:list) -> None:
        self.content = arr
    
    def __len__(self) -> int:
        return len(self.content)

    def partition(self, left_pointer, right_pointer):
        pivot_index = right_pointer
        pivot = self.content[pivot_index]
        right_pointer -= 1

        while True:
            while self.content[left_pointer] < pivot:
                left_pointer += 1
            
            while self.content[right_pointer] > pivot:
                right_pointer -= 1

            if left_pointer >= right_pointer:
                break
            else:
                self.content[left_pointer], self.content[right_pointer] = self.content[right_pointer], self.content[left_pointer]
                left_pointer += 1
        
        self.content[left_pointer], self.content[pivot_index] = self.content[pivot_index], self.content[left_pointer]

        return left_pointer

    # Quicksort
    def quicksort(self, left_index, right_index):
        # caso base
        if right_index - left_index <= 0:
            return
        
        pivot_index = self.partition(left_index, right_index)
        self.quicksort(left_index, pivot_index - 1)
        self.quicksort(pivot_index + 1, right_index)

    def quickselect(self, kth_lowest_value, left_index, right_index):
        # caso base
        if right_index - left_index <= 0:
            return self.content[left_index]

        pivot_index = self.partition(left_index, right_index)

        if kth_lowest_value < pivot_index:
            # executa recursivamente à esquerda
            self.quickselect(kth_lowest_value, left_index, pivot_index - 1)
        elif kth_lowest_value > pivot_index:
            self.quickselect(kth_lowest_value, pivot_index + 1, right_index)
        else:
            return self.content[pivot_index]

        

sortarr = SortableArray([20, 1, 3, 22, 102, 7])

# Assumindo que left e right pointer são as extremidades:
sortarr.partition(0, len(sortarr.content) - 1)
# ao final da partição, todos os valores menores que o pivo estarão à esquerda e todos os maiores à direita

# IMPLEMENTANDO MERGESORT EM PYTHON
# Tem eficiência exata de O(N*logN)
# O quicksort é mais eficiente pois não tem chamadas recursivas tão profundas

def merger(xs:list, ys:list)->list:
    if xs == [] and ys == []:
        return []
    elif xs == []:
        return ys
    elif ys == []:
        return xs
    else:
        if xs[0] <= ys[0]:
            return [xs[0]] + merger(xs[1:], ys)
        else:
            return [ys[0]] + merger(xs, ys[1:])
        
def merge_sort(xs:list)->list:
    if len(xs) <= 1:
        return xs
    else:
        meio = len(xs) // 2
        us = xs[:meio]
        vs = xs[meio:]
        return merger(merge_sort(us), merge_sort(vs))

# Exemplos aleatórios para testar
def make_random_size_list(N: int) -> list:
    randomlist = []

    for i in range(N):
        randomlist.append(randint(0, 100))
    
    return randomlist

pequena = make_random_size_list(100)
media = make_random_size_list(1000)
grande = make_random_size_list(10000)

# Função simplificada do Quicksort

def quicksort(ls):
    obj = SortableArray(ls)
    obj.quicksort(0, len(ls) - 1)
    return obj.content

# Exercícios
# Q1: Função para calcular o produto dos 3 maiores números da array

def tres_maior_produto(array:list)->float:
    array.sort() # Não usamos nem mergesort nem quicksort pq o Timsort é mais rapido
    return array[-1] * array[-2] * array[-3]

# Q2: Usar sorting para criar uma função que identifica qual número está faltando na sequencia

def find_missing_number(array:list)->int:
    array.sort()
    succ = lambda x, y: x + 1 == y
    for i in range(len(array)):
        if not succ(array[i], array[i+1]):
            return array[i] + 1
    
    return None

find_missing_number([4, 1, 2]) # resulta em 3

# Q3: Função para achar o maior número duma lista
# Uma implementação O(N²):
def inef_greatest(array:list):
    for i in array:
        for j in array:
            if i < j:
                break
            else:
                return i

# Uma implementação O(N):
def linear_greatest(array:list):
    greatest = array[0]
    for i in array:
        if i > greatest:
            greatest = i

    return greatest

# Uma implementação O(N*LogN):
def nlogn_greatest(array:list):
    array = quicksort(array)
    return array[-1]