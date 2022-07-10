# Q3 Soma cumulativa de low até high
# Ex: sum_recursive(3, 5) -> (3 + 4 + 5) = 12
def sum_recursive(low:int, high:int)->int:
    if high == low:
        return low
    return high + sum_recursive(low, high - 1)

# Q4: Função que printa recursivamente todos os números numa array aninhada em qualquer nível

def prints_numbers(nested_arr: str)-> None:
    for elem in nested_arr:
        if not isinstance(elem, list):
            print(elem)
        else:
            prints_numbers(elem)