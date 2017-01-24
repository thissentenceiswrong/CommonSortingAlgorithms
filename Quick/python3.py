def quick_sort(arr):
    def helper(arr, low, high):
        if not low < high:
            return

        iPivot = low
        iTmp = iPivot + 1

        for i in range(iPivot + 1, high):
            # Swap if current valve is smaller than pivot
            # Actually swap the valve that bigger than pivot out
            if arr[i] < arr[iPivot]:
                arr[i], arr[iTmp] = arr[iTmp], arr[i]
                iTmp += 1

        # Swap pivot to the middle(relativly)
        arr[iPivot], arr[iTmp - 1]\
            = arr[iTmp - 1], arr[iPivot]

        helper(arr, low, iTmp - 1)
        helper(arr, iTmp, high)
        return arr

    return helper(arr, 0, len(arr))


if __name__ == '__main__':
    var = [5, 2, 3, 8, 4, 7, 1, 9, 6]
    print(quick_sort(var))
