# EXERCISES
# Q1: O(N) pois cria uma nova array collection de tamanho N
# Q2: O(N)
# Q3:
def reverse_arr(array:list):
    meio = len(array) // 2
    for i in range(meio+1):
        array[i], array[-(i+1)] = array[-(i+1)], array[i]
    
    return array

# Q4:
# V1:  O(N) e O(N)
# V2: O(N) e O(1)
# V3: O(N) e O(N) <- devido ao callstack

