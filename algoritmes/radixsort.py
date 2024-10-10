"""Implementation of LSD Radixsort"""
def radixsort(array: list[int], num_length: int) -> list[int]:
    """Sorts list of integers using the LSD Radixsort algorithm"""
    one_array: list = []
    zero_array: list = []

    for digit in range(num_length):
        for num in array:
            # Put num in one_array if n-th binary digit is 1,
            # otherwise put it in zero_array
            if num >> digit & 1:
                one_array.append(num)
            else:
                zero_array.append(num)
        array = zero_array + one_array
        zero_array, one_array = [], []
    return array

def main() -> None:
    array: list = eval(input())
    num_length: int = int(input())
    radixsort(array, num_length)

if __name__ == "__main__":
    main()