from inspect import currentframe
from multiprocessing.dummy import current_process
from re import S


class Stack:
    def __init__(self) -> None:
        self.__data = []

    def __repr__(self) -> str:
        return str(self.__data)

    def pop(self):
        self.__data.pop()
    
    def push(self, elem) -> None:
        self.__data.append(elem)
    
    def read(self):
        return self.__data[-1]

    def __len__(self):
        return len(self.__data)

    def __str__(self):
        return ''.join(self.__data)

my_stack = Stack()
my_stack.push(10)
my_stack.push(100)
my_stack.push(1000)
print(my_stack.read())


# Perceba que como Python não cumpre/faz cumprir a encapsulação, a expressão abaixo é totalmente válida
# Ainda que totalmente contra a intenção de um stack:
# my_stack._Stack__data = [1, 2, 3] + my_stack._Stack__data

# Objetivo: Implementar uma função de linting para verificar algum erro de sintaxe
# Ex: x = 10, 90) <- erro de sintaxe

def syntax_error(line_of_code: str)->bool:
    """Verifica se uma linha de código no formato de string tem algum erro na sintaxe por não fechar algum dos símbolos usuais
    ex: (a = [1, 2]} -> True
    ex: (a = [1, 2]) -> False"""

    symbols = {")":"(",
            "}":"{",
            "]":"["}

    symbol_stack = Stack()

    for l in line_of_code:
        if l in symbols.values():
            symbol_stack.push(l)
        elif (l in symbols) and (symbol_stack.read() == symbols[l]):
            symbol_stack.pop()
        elif (l not in symbols):
            continue
        else: 
            return True
    
    # Se ainda tiver elementos no stack
    if len(symbol_stack) != 0:
        return True
    return False

# Deve retornar True
print(syntax_error('array = ["this", "is", "incomplete"'))
# Deve retornar False
print(syntax_error('array = ["this", "is", "complete"]'))

# QUEUES: First In, First Out:

class Queue:
    def __init__(self) -> None:
        self.__data = []

    def __repr__(self) -> str:
        return str(self.__data)
    
    def enqueue(self, element):
        self.__data.append(element)
    
    def dequeue(self):
        first = self.read()
        self.__data = self.__data[1:]
        return first
    
    def read(self):
        return self.__data[0]

    def __len__(self):
        return len(self.__data)

fila_de_cinema = Queue()
fila_de_cinema.enqueue("João")
fila_de_cinema.enqueue("Maria")
fila_de_cinema.enqueue("Tiago")

fila_de_cinema.dequeue() # João é o primeiro a sair

print(fila_de_cinema)

# Q1: Software de um call center para atender clientes: Queue
# Q2: Se colocassemos num stack: 1, 2, 3, 4, 5 e 6, depois chamassemos pop 2x,
# qual numero seria lido com read? R: 4

# Q3: Repetir o mesmo comportamente da Q2 com uma queue, qual seria o número lido?
# R: 3

# Q4: Usar stack pra implementar uma função que reverte uma string

def my_reverse(string:str)->str:
    result = Stack()
    currrent_index = 1

    while currrent_index < (len(string) + 1):
        result.push(string[-currrent_index])
        currrent_index += 1

    return str(result)

print(my_reverse("Flamengo"))