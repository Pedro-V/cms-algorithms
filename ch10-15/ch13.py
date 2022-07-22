# Implementando uma classe com método de partição simples
def swap(a, b):
    a, b = b, a

class SortableArray:
    def __init__(self, arr:list) -> None:
        self.content = arr

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
        

sortarr = SortableArray([20, 1, 3, 22, 102, 7])

# Assumindo que left e right pointer são as extremidades:
sortarr.partition(0, len(sortarr.content) - 1)
# ao final da partição, todos os valores menores que o pivo estarão à esquerda e todos os maiores à direita