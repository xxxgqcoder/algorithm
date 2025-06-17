# insert sort
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


# quick sort
def median3(a, left, right):
    """
    Find pivot value from left, middle and right position of a.
    """
    # sort left, mid, right
    mid = (left + right) // 2
    if a[mid] < a[left]:
        a[left], a[mid] = a[mid], a[left]
    if a[right] < a[left]:
        a[right], a[left] = a[left], a[right]
    if a[right] < a[mid]:
        a[mid], a[right] = a[right], a[mid]
    # put a[mid] to right-1 and return a[right-1] as pivot value
    a[mid], a[right - 1] = a[right - 1], a[mid]
    return a[right - 1]


def partition(a, left, right):
    pivot = median3(a, left, right)
    if right - left <= 2:
        return (left + right) // 2

    # initially a[j] = pivot, since pivot is put at right - 1
    i, j = left, right - 1
    while i < j:
        while True:
            i += 1
            if a[i] >= pivot:  # i will at most stop at right - 1, since a[right-1] = pivot after median3
                break
        while True:
            j -= 1
            if a[j] <= pivot:  # j will at least stop at left, as a[left] <= a[right-1] after median3
                break
        if i < j:
            a[i], a[j] = a[j], a[i]
    # a[i] >= pivot
    a[i], a[right - 1] = a[right - 1], a[i]
    return i


def quick_sort(a, left, right):
    if left >= right:
        return
    i = partition(a, left, right)
    quick_sort(a, left, i - 1)
    quick_sort(a, i + 1, right)


# quick sort v2
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
