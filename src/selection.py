def select_sort(arr):
    """
    Each loop finds the smallest value and swap it with the front of list
    """
    for index_head in range(len(arr)):
        index_smallest = index_head
        for current in range(index_head, len(arr)):
            if arr[index_smallest] > arr[current]:
                index_smallest = current
        # Swap
        arr[index_smallest], arr[index_head] = arr[index_head], arr[index_smallest]

    return arr
