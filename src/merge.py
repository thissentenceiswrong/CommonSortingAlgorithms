import math


def merge_sort(arr):
    """
    Merge Sort

    Split list into multi-lists and pick the smallest from them
    """

    def merge(arr1, arr2):
        """
        Compare and Merge
        """
        arr_ret = list()

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
    l_list = arr[0:math.floor(len(arr) / 2)]
    r_list = arr[math.floor(len(arr) / 2):]

    l_list = merge_sort(l_list)
    r_list = merge_sort(r_list)

    return merge(l_list, r_list)
