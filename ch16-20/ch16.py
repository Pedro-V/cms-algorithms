# Priority Queues: Semelhante a uma Fila, mas respeitando princípios de ordered arrays na inserção
# Binary max-heap
# Apesar de heaps serem um tipo de árvore binária, sua implementação como arrays facilita solucionar o problem do último nó
from numpy import tri


class Heap:
    def __init__(self) -> None:
        self.data = []

    def root_node(self):
        return self.data[0]
    def last_node(self):
        return self.data[-1]
    
    def left_child_index(index):
        return (index * 2) + 1
    def right_child_index(index):
        return (index * 2) + 2
    def parent_index(index):
        return (index - 1) // 2 # deve ser um valor inteiro para permitir indexing
# Implementar as operações de inserção e deleção num heap necessariamente envolve solucionar o problema de localizar o "último nó"
# Último nó: Aquele em que, no último row do heap, é o mais à direita e é não-vazio

# Saber o último nó é importante num heap porque garante que ele estará balanceado. Se estiver balanceado, permite que esteja "completo"
# se estiver completo, é possível realizar as operações com eficiência O(log N)

# Na inserção de um novo valor, esse novo valor obrigatoriamente será o novo last_node e 
    def insert(self, value):
        self.data.append(value)

        new_node_index = len(self.data) - 1

        # vamos subindo e substituindo ao longo do heap enquanto o valor pai for menor que o novo valor filho
        while new_node_index > 0 and self.data[new_node_index] > self.data[self.parent_index(new_node_index)]:
            self.data[self.parent_index(new_node_index)], self.data[new_node_index] = self.data[new_node_index], self.data[self.parent_index(new_node_index)]
            # Novo índice "sobe" um row e se torna o pai
            new_node_index = self.parent_index(new_node_index)
# Implementando deleção com métodos auxiliares

    def has_greater_child(self, index):
        # checa se um nó no índice dado possui algum filho com valor maior que o seu próprio
        arr = self.data
        val = arr[index]
        if len(arr) >= index + 2:
            left = arr[self.left_child_index(index)]
            right = arr[self.right_child_index(index)]
            return left > val or right > val
        return False

    def calculate_larger_child_index(self, index):
        # retorna o índice do nó filho de maior valor:
        left = self.left_child_index(index)
        right = self.right_child_index(index)
        # Cada tupla contém (valor, indice) para cada lado
        l_tuple  = self.data[left], left
        r_tuple  = self.data[right], right
        return (max(r_tuple, l_tuple))[1]
    
    # sempre deletamos o nó raiz
    # O algoritmo é trickle down: Começamos deletando o nó raiz, substituindo ele pelo último nó
    # e esse novo nó raiz irá sendo "abaixado" conforme for encontrando valores maiores que ele
    def delete(self):
        # a array/heap agora terá como raiz o último nó, que já não existe mais no final do heap
        self.data = self.data[-1] + self.data[1:-1]

        trickle_node_index = 0
        # Enquanto o nó pai tem algum
        while self.has_greater_child(trickle_node_index):
            larger_child_index = self.calculate_larger_child_index(trickle_node_index)
            # Se o nó trickle atual ter algum filho com valor maior, troque pelo nó de maior valor e recursivamente desça um row
            self.data[larger_child_index], self.data[trickle_node_index] = self.data[trickle_node_index], self.data[larger_child_index]

            trickle_node_index = larger_child_index

# Como heaps permitem operações O(Log N) e sempre permitem a deleção do maior valor e a inclusão ordenada de valores, eles 
# são uma ótima implementação para filas de prioridade (Priority Queues)

# EXERCICIOS
# Q1
"""na forma    array/heap: [11, 
                        10,     8, 
                      6,   9,  7, 4, 
                    2, 1, 3, 5]
"""

# Q2:
"""na forma    array/heap: [10, 
                        9,     8, 
                      6,   5,  7, 4, 
                    2, 1, 3, ]

                    Ou seja, igual ao heap inicial
"""

# Q3
"""na forma    array/heap: [99, 
                        22,     68, 
                      10, 2,  34, 55]

ou, numa array tradicional: [99, 22, 68, 10, 2, 35, 55]
"""