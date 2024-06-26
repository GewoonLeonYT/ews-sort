def radix_sort(array: list[int], num_length: int) -> list[int]:
    one_array: list = []
    zero_array: list = []

    for digit in range(num_length):
        for num in array:
            """
            Put num in one_array if n-th binary digit is 1,
            otherwise put it in zero_array
            """
            if num >> digit & 1:
                one_array.append(num)
            else:
                zero_array.append(num)
        array = zero_array + one_array
        zero_array, one_array = [], []
    return array