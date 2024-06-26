def radix_sort(array: list[int], num_length: int):
    one_array = []
    zero_array = []

    for digit in range(num_length):
        for num in array:
            if num >> digit & 1:
                one_array.append(num)
            else:
                zero_array.append(num)
        array = zero_array + one_array
        zero_array, one_array = [], []
    return array