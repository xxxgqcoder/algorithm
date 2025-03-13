def insert_sort(a):
    for j in range(1, len(a)):
        # assume a[0, ..., j-1] is sorted
        key = a[j]  # make a hole at a[j]
        i = j - 1
        while i >= 0 and a[i] > key:
            # initial case: a[j-1] > a[j], move hole one step left
            a[i + 1] = a[i]
            i = i - 1
        # termination:
        # i >= 0, a[i] < key, i+1 is the place for key (hole)
        # i < 0, all values checked, i = 0 is the place for key (hole)
        a[i + 1] = key


def insert_sort_v2(a):
    if len(a) <= 1:
        return

    for p in range(1, len(a)):
        tmp = a[p]
        j = p
        while j > 0 and a[j - 1] > tmp:
            a[j] = a[j - 1]
            j = j - 1
        a[j] = tmp


def median3(a, left, right):
    center = (left + right) // 2
    if a[center] < a[left]:
        a[left], a[center] = a[center], a[left]
    if a[right] < a[left]:
        a[right], a[left] = a[left], a[right]
    if a[right] < a[center]:
        a[right], a[center] = a[center], a[right]
    a[center], a[right - 1] = a[right - 1], a[center]
    return a[right - 1]


def partition(a, left, right):
    pivot = median3(a, left, right)
    if right - left <= 2:
        return (left + right) // 2
    i, j = left, right - 1
    while i < j:
        while True:
            i += 1  # at least move forward one step, in case a[i] = pivot
            if a[i] >= pivot:
                break
        while True:
            j -= 1  # at least move backward one step, in case a[j] = pivot
            if a[j] <= pivot:
                break
        if i < j:
            a[i], a[j] = a[j], a[i]
    a[i], a[right - 1] = a[right - 1], a[i]
    return i


def quick_sort(a, left, right):
    if len(a) <= 1 or left >= right:
        return
    i = partition(a, left, right)
    quick_sort(a, left, i - 1)
    quick_sort(a, i + 1, right)


def partition_v2(a, p, r):
    x = a[r]
    i = p - 1
    for j in range(p, r):
        if a[j] <= x:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[r] = a[r], a[i + 1]
    return i + 1


def quick_sort_v2(a, left, right):
    if len(a) <= 1 or left >= right:
        return

    p = partition_v2(a, left, right)
    quick_sort_v2(a, left, p - 1)
    quick_sort_v2(a, p + 1, right)
