def bubble_sort(arr):
    # lop goes reversed
    for lop in reversed(range(len(arr))):
        for lop2 in range(lop):
            if arr[lop2] > arr[lop2 + 1]:
                # Swap
                (arr[lop2], arr[lop2 + 1]) \
                    = (arr[lop2 + 1], arr[lop2])

    return arr

if __name__ == '__main__':
    arr = [3,9,1,2,4,8,6,7,0,5]
    print(bubble_sort(arr))
    print(arr)
