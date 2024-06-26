from heapq import heappop, heappush

def heap_sort(array: list[int]) -> list[int]:
    output = []
    for num in array:
        heappush(output, num)
    return [heappop(output) for _ in range(len(output))]
