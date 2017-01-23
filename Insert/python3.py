def insert_sort(arr):
    for index in range(1, len(arr)):
        current = arr[index]
        position = index

        while position > 0 and arr[position - 1] > current:
            arr[position] = arr[position - 1]
            position -= 1

        arr[position] = current

    return arr


if __name__ == '__main__':
    var = [5, 6, 8, 9, 0, 4, 3, 7, 2, 1]
    print(insert_sort(var))
