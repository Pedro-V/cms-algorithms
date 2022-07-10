def number_of_paths(n):
    if n < 0:
        return 0
    elif n == 1 or n == 0:
        return 1
    else:
        return number_of_paths(n - 1) + number_of_paths(n - 2) + number_of_paths(n - 3)

def count_chars(words:list)-> int:
    counter = 0
    for member in words:
        if isinstance(member, list):
            count_chars(member)
        else:
            counter += 1

    return counter