def merge_sort(arr):
    """
    Merge Sort

    Split list into multi-lists and pick the smallest from them

    Complexity:
    Time: 
    Space: 
    """
    def merge(arr1, arr2):
        """
        Compare and Merge
        """
        arr_ret = []

        cur1 = 0
        cur2 = 0
        while cur1 < len(arr1) and cur2 < len(arr2):
            if arr1[cur1] < arr2[cur2]:
                arr_ret.append(arr1[cur1])
                cur1 += 1
            else:
                arr_ret.append(arr2[cur2])
                cur2 += 1

        while cur1 < len(arr1):
            arr_ret.append(arr1[cur1])
            cur1 += 1

        while cur2 < len(arr2):
            arr_ret.append(arr2[cur2])
            cur2 += 1

        return arr_ret

    if len(arr) == 1:
        return arr

    # Equally split arr into halves
    index_halve = len(arr) // 2
    l_list = arr[0:index_halve]
    r_list = arr[index_halve:]

    l_list = merge_sort(l_list)
    r_list = merge_sort(r_list)

    return merge(l_list, r_list)


if __name__ == "__main__":
    samples = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [9, 8, 7, 6, 5, 4, 3, 2, 1],
        [5, 1, 7, 2, 3, 9, 8, 4, 6],
        [2, 2, 2, 1, 1, 1, 5, 5, 5]
    ]

    for sample in samples:
        print(merge_sort(sample))
