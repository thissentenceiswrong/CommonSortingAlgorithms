def select_sort(arr):
    for index_head in range(len(arr)):
        index_smallest = index_head
        for current in range(index_head, len(arr)):
            if arr[index_smallest] > arr[current]:
                index_smallest = current
        # Swap
        (arr[index_smallest], arr[index_head])\
            = (arr[index_head], arr[index_smallest])

    return arr


if __name__ == '__main__':
    var = [6, 1, 5, 2, 7, 8, 9, 3, 4, 0]
    print(select_sort(var))
