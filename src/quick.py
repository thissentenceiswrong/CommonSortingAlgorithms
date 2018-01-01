def quick_sort(arr):
    """
    Quick Sort

    Split & Sort
    """
    def helper(arr, low, high):
        if not low < high:
            return

        index_pivot = low
        index_tmp = index_pivot + 1

        for i in range(index_pivot + 1, high):
            # Swap if current valve is smaller than pivot
            # Actually swap the valve that bigger than pivot out
            if arr[i] < arr[index_pivot]:
                arr[i], arr[index_tmp] = arr[index_tmp], arr[i]
                index_tmp += 1

        # Swap pivot to the middle(relativly)
        arr[index_pivot], arr[index_tmp - 1] \
            = arr[index_tmp - 1], arr[index_pivot]

        helper(arr, low, index_tmp - 1)
        helper(arr, index_tmp, high)
        return arr

    return helper(arr, 0, len(arr))
