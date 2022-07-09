# Q1: A função abaixo tem eficiência O(N):

def one_hunder_sum(array: list)->bool:
    left_index = 0
    right_index = len(array) - 1
    while left_index < len(array) / 2:
        if array[left_index] + array[right_index] != 100:
            return False
        
        left_index += 1
        right_index -= 1
    return True

# Q2: A função abaixo tem eficiência O(N). Onde N = N1 + N2. N1 e N2 são os tamanhos de cada array

def merge(arr1:list, arr2:list)->list:
    new_arr = []
    arr1_pointer = 0
    arr2_pointer = 0

    while arr1_pointer < len(arr1) or arr2_pointer < len(arr2):
        # Se tiver chegado no final da arr1
        if arr1_pointer == len(arr1):
            new_arr.append(arr2[arr2_pointer])
            arr2_pointer += 1
        # Se tiver no final da arr2
        elif arr2_pointer == len(arr2):
            new_arr.append(arr1[arr1_pointer])
            arr1_pointer += 1
        # Se o numero atual da arr1 for menor
        elif arr1[arr1_pointer] < arr2[arr2_pointer]:
            new_arr.append(arr1[arr1_pointer])
            arr1_pointer += 1
        else:
            new_arr.append(arr2[arr2_pointer])
            arr2_pointer += 1
    
    return new_arr


# Q3: O algoritmo é O(N), com N = N1 (tamanho da string needle) * N2 (tamanho da string haystack)

def find_needle(needle:str, haystack:str)->bool:
    needle_index = 0
    haystack_index = 0

    while haystack_index < len(haystack):
        if needle[needle_index] == haystack[haystack_index]:
            found_needle = True
            
            while needle_index < len(needle):
                if needle[needle_index] != haystack[haystack_index + needle_index]:
                    found_needle = False
                    break
                needle_index += 1
            if found_needle:
                return True
            needle_index = 0
        haystack_index += 1
    
    return False

# Q4: O algoritmo abaixo é O(N), pois as iterações vão aumentando linearmente conforme
# o tamanho da array

def largest_product(array:list)->float:
    largest_product_so_far = array[0] * array[1] * array[2]
    i = 0
    while i < len(array):
        j = i + 1
        while j < len(array):
            k = j + 1
            while k < len(array):
                if array[i] * array[j] * array[k] > largest_product_so_far:
                    largest_product_so_far = array[i] * array[j] * array[k]
                k += 1
            j += 1
        i += 1
    
    return largest_product_so_far


# A eficiência do algoritmo abaixo é O(log N):
# Se dermos uma array de 4 strings, ele leva 2 passos
# Se dobramos o tamanho da array para 8 strings, ele leva 3 passos
# Com 16 strings, 4 passos
def pick_resume(resumes):
    eliminate = "top"
    while len(resumes) > 1:
        if eliminate == "top":
            resumes = resumes[len(resumes) // 2:]
            eliminate = "bottom"
        else:
            resumes = resumes[:len(resumes) // 2]
            eliminate = "top"
    
    return resumes[0]