def bubble_sort(arr):
    """
    Bubble Sort

    Each loop brings the biggest value to the end of the array

    Complexity:
    Time: 
        Average:
        Worst:
    Space: 
    """
    # lop goes reversed
    for lop in reversed(range(len(arr))):
        for lop2 in range(lop):
            if arr[lop2] > arr[lop2 + 1]:
                # Swap
                (arr[lop2], arr[lop2 + 1]) \
                    = (arr[lop2 + 1], arr[lop2])

    return arr
