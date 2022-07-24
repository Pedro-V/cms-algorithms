# Árvores Binárias de Busca
from math import log2


class TreeNode:
    def __init__(self, val, left=None, right=None) -> None:
        self.value = val
        self.leftChild = left
        self.rightChild = right

    def __repr__(self) -> str:
        return f"({self.leftChild.__repr__()} <- {self.value} -> {self.rightChild.__repr__()})"
    
    def empty(self)->bool:
        return self.leftChild == None and self.rightChild == None

def search_tree(tree_beginning:TreeNode, searched_value):
    if tree_beginning == None or searched_value == tree_beginning.value:
        return tree_beginning 
    elif searched_value > tree_beginning.value:
        return search_tree(tree_beginning.rightChild, searched_value)
    else:
        return search_tree(tree_beginning.leftChild, searched_value)

# Assumindo que valores iguais serão armazenados à esquerda
def insert_tree(node:TreeNode, value):
    if value is None:
        return

    if value > node.value:
        # Se um nó não tiver filhos, crie um novo com o valor a ser inserido
        if node.rightChild is None:
            node.rightChild = TreeNode(value)
            return node.rightChild
        # caso contrário, penetre recursivamente
        return insert_tree(node.rightChild, value)
    else:
        if node.leftChild is None:
            node.leftChild = TreeNode(value)
            return node.leftChild
        return insert_tree(node.leftChild, value)

# Node é o filho direito do nó que terá seu valor removido
# value é o valor a ser removido
def find_sucessor_node_value(node:TreeNode, value):
    while (node.leftChild is not None):
        node = node.leftChild
    return node.value

def remove_tree(node:TreeNode, value_to_remove):
    if node is None:
        return
    elif value_to_remove > node.value:
        node.rightChild = remove_tree(node.rightChild, value_to_remove)
        return node
    elif value_to_remove < node.value:
        node.leftChild = remove_tree(node.leftChild, value_to_remove)
        return node
    else:
        # Se o nó que contém o valor a ser removido não tiver filhos, apenas o anule
        if node.empty():
            node = None
            return node
        elif node.rightChild is None and node.leftChild is not None:
            node = node.leftChild
            return node 
        else:
            successor_val = find_sucessor_node_value(node.rightChild, value_to_remove)
            node.value = successor_val
            node.rightChild = remove_tree(node.rightChild, successor_val)
            return node

root = TreeNode(50, TreeNode(25), TreeNode(75))
for i in [11, 33, 30, 40, 75, 61, 89, 55, 82, 95, 52]:
    insert_tree(root, i)
root = remove_tree(root, 55)

def traverse_and_print(node:TreeNode):
    if node is None:
        return
    traverse_and_print(node.leftChild)
    print(node.value)
    traverse_and_print(node.rightChild)

# EXERCICIOS
# Q1
"""
    1
       5
    2     9
     4  6  10
   3     8
"""

# Q2
print(log2(1000)) # 10 passos

# Q3
def greatest_val_tree(node:TreeNode):
    while (node.rightChild is not None):
        node = node.rightChild
    return node.value

# Q4 Preorder:
def traverse_and_print(node):
    if node is None:
        return
    print(node.value)
    traverse_and_print(node.leftChild)
    traverse_and_print(node.rightChild)
"""
O output com os livros será:
Moby Dick
Great Expectations
Alice in Wonderland
Lord of the Flie
Robinson Crusoe
Pride and Prejudice
The Odyssey
"""
