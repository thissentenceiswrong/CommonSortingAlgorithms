def quick_sort(arr):
    """
    Quick Sort

    Split & Sort

    Complexity:
    Time: 
    Space: 
    """
    def helper(arr, low, high):
        if not low < high:
            return

        # Randomly pick a pivot (low in this example)
        index_pivot = low
        # Swap value that is < pivot with this index
        index_tmp = index_pivot + 1

        # Move value that are smaller than pivot forward
        for i in range(index_pivot + 1, high):
            if arr[i] < arr[index_pivot]:
                arr[i], arr[index_tmp] = arr[index_tmp], arr[i]
                index_tmp += 1

        # Swap pivot with the last value <= pivot
        arr[index_pivot], arr[index_tmp - 1] \
            = arr[index_tmp - 1], arr[index_pivot]

        helper(arr, low, index_tmp - 1)
        helper(arr, index_tmp, high)
        return arr

    return helper(arr, 0, len(arr))


if __name__ == "__main__":
    samples = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [9, 8, 7, 6, 5, 4, 3, 2, 1],
        [5, 1, 7, 2, 3, 9, 8, 4, 6],
        [2, 2, 2, 1, 1, 1, 5, 5, 5]
    ]

    for sample in samples:
        print(quick_sort(sample))
