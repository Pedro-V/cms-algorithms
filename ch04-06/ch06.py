# Poderia usar in, mas definindo contains, que é O(N) no worst-case (não conter):
def contains(elem, array:list)->bool:
    for i in array:
        if elem == i:
            return True


def intersection(firstArray:list, secondArray:list)->list:
    result = []
    # poderia incluir aqui uma condição para iterar primeiro sobre a array de menor tamanho
    for i in firstArray:
        # se já for computado, vai pro próximo i
        # verificar se um i já está no resultado é sempre mais rápido que o elif
        if contains(i, result):
            continue
        elif contains(i, secondArray):
            result.append(i)
        else:
            continue

    return result

# Q3: A função abaixo checa se um array numérica contém 2 pares de números distintos que somados dá 10
# Dada uma array [x1, x2 ... xn-1, xn], os seus cases seriam:
# best-case: onde x1 + x2 = 10
# average-case: onde xi e xj estão no meio da array e xi+xj = 10
# worst-case: não existem xi e xj tal que xi+xj = 10

def two_sum(array:list)->bool:
    for i in array:
        for j in array:
            return (i != j and (i + j == 10))
    return False

# Dada uma função para verificar se um "X" maiúsculo está contido numa string,
# otimizar a função para os cenários best-case e average-case

# A função abaixo é O(N) para todos os cenários
def containsX(string:str)->bool:
    foundX = False

    for i in string:
        if i == "X":
            foundX = True
    
    return foundX

# Otimizando...
def optimized_containsX(string:str)->bool:
    for i in string:
        if i == "X":
            # Interrompe o loop no primeiro match
            return True

    return False