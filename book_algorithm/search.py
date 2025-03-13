def binary_search(a, x):
    if len(a) < 1:
        return -1

    i, j = 0, len(a) - 1
    while i <= j:
        mid = (i + j) // 2
        if a[mid] == x:
            return mid
        elif a[mid] > x:
            j = mid - 1
        else:
            i = mid + 1
    return -1
