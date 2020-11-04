def insert_sort(arr):
    """
    Insertion Sort

    Each loop picks next element and inserts it into already sorted list

    Complexity:
    Time: 
    Space: 
    """
    for index in range(1, len(arr)):
        current = arr[index]
        cursor = index

        while cursor > 0 and arr[cursor - 1] > current:
            arr[cursor] = arr[cursor - 1]
            cursor -= 1

        arr[cursor] = current

    return arr
