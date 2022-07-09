def linear_search(array: list, search_value: int) -> int:
    for index, val in enumerate(array):
        if val == search_value:
            return index
        elif val > search_value:
            break

def binary_search(array: list, search_value: int) -> int:
    lower_bound = 0
    upper_bound = len(array) - 1
    while (lower_bound <= upper_bound):
        midpoint = int((upper_bound + lower_bound) / 2)

        value_at_midpoint = array[midpoint]
        if search_value == value_at_midpoint:
            return midpoint
        elif search_value < value_at_midpoint:
            upper_bound = midpoint - 1
        else:
            lower_bound = midpoint + 1
