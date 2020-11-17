# [left, right)
def quick_sort(arr, left, right):
    if not left < right:
        return

    index_pivot = left
    index_tmp = index_pivot + 1

    for i in range(index_tmp, right):
        if arr[i] < arr[index_pivot]:
            # swap
            arr[i], arr[index_tmp] = arr[index_tmp], arr[i]
            index_tmp += 1

    # swap pivot
    arr[index_pivot], arr[index_tmp - 1] = arr[index_tmp - 1], arr[index_pivot]

    quick_sort(arr, left, index_tmp - 1)
    quick_sort(arr, index_tmp, right)


if __name__ == "__main__":
    samples = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [9, 8, 7, 6, 5, 4, 3, 2, 1],
        [5, 1, 7, 2, 3, 9, 8, 4, 6],
        [2, 2, 2, 1, 1, 1, 5, 5, 5]
    ]

    for sample in samples:
        print(quick_sort(sample, 0, len(sample))
