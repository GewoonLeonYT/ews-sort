#!/usr/bin/env python3
"""Generate lists"""
import sys
import random

def random_list(number_of_elements: int, max_int: int) -> list:
    """Return a random list"""
    array = []
    for _ in range(number_of_elements):
        array.append(random.randint(0, max_int + 1))
    return array

def sequential_list(number_of_elements: int) -> list:
    """Return an ordered list beginning at zero"""
    return list(range(number_of_elements))

def similar_list(number_of_elements: int, max_int: int) -> list:
    """Return a list with few unique elements"""
    if max_int > number_of_elements:
        raise ValueError("number_of_elements has to be more than max_int")
    elif number_of_elements % (max_int + 1) != 0:
        raise ValueError("number_of_elements should be multiple of max_int + 1")
    array = sequential_list(max_int + 1)
    array *= number_of_elements // (max_int + 1)
    random.shuffle(array)
    return array
    
def unique_list(number_of_elements: int) -> list:
    """Generate a shuffled list with no repeating elements"""
    array = sequential_list(number_of_elements)
    random.shuffle(array)
    return array
    
def reversed_list(array: list) -> list:
    """Return the reversed list"""
    return array[::-1]


def main() -> None:
    """main function"""
    args = sys.argv[1:]

    list_type = args[0]
    number_of_elements = int(args[1])
    
    match list_type:
        case "random":
            max_int = int(args[2])
            print(random_list(number_of_elements, max_int))
            print(max_int.bit_length())
        case "sequential" | "sorted":
            print(sequential_list(number_of_elements))
            print((number_of_elements - 1).bit_length())
        case "reversed_sequential" | "reverse_sorted":
            print(reversed_list(sequential_list(number_of_elements)))
            print((number_of_elements - 1).bit_length())
        case "unique":
            print(unique_list(number_of_elements))
            print((number_of_elements - 1).bit_length())
        case "similar":
            max_int = int(args[2])
            print(similar_list(number_of_elements, max_int))
            print(max_int.bit_length())

if __name__ == "__main__":
    main()
