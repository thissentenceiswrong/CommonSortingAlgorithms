def merge_sort(arr):
    # Do the actual comparision work
    def merge(arr1, arr2):
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

    # Split arr
    l_list = arr[0:int(len(arr) / 2 + 0.5)]
    r_list = arr[int(len(arr) / 2 + 0.5):len(arr)]

    l_list = merge_sort(l_list)
    r_list = merge_sort(r_list)

    return merge(l_list, r_list)


if __name__ == '__main__':
    var = [6, 5, 1, 4, 2, 8, 9, 7, 3]
    print(merge_sort(var))
