"""Implementation of heapsort"""
from heapq import heappop, heappush

def heapsort(array: list[int]) -> list[int]:
    """Sorts list using the heapsort algorithm"""
    output: list = []
    for num in array:
        heappush(output, num)
    return [heappop(output) for _ in range(len(output))]
