def bubble_sort(items: list) -> list:
    size = len(items) - 1
    for i in range(size):
        for j in range(size - i):
            if items[j] > items[j + 1]:
                swap(items, j, j + 1)

    return items


def selection_sort(items):
    size = len(items)
    for i in range(size):
        min_index = i
        for j in range(i + 1, size):
            if items[j] < items[min_index]:
                min_index = j

        if min_index != i:
            swap(items, i, min_index)

    return items


def insertion_sort(items):
    size = len(items)
    for i in range(1, size):
        for j in range(i, 0, -1):
            if items[j - 1] > items[j]:
                swap(items, j, j-1)
            else:
                break

    return items


def quick_sort(items, low, high):
    def partition(items, start, end):
        pivot = (start + end) // 2
        swap(items, pivot, end)

        i = start

        for j in range(start, end):
            if items[j] <= items[end]:
                swap(items, i, j)
                i += 1

        swap(items, i, end)

        return i

    if low >= high:
        return

    pivot = partition(items, low, high)
    quick_sort(items, low, pivot - 1)
    quick_sort(items, pivot + 1, high)


def swap(items, index_1, index_2):
    items[index_1], items[index_2] = items[index_2], items[index_1]

    return items


def merge_sort(items):
    if len(items) == 1:
        return

    middle = len(items) // 2

    left = items[:middle]
    right = items[middle:]

    merge_sort(left)
    merge_sort(right)

    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            items[k] = left[i]
            i += 1
        else:
            items[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        items[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        items[k] = right[j]
        j += 1
        k += 1


def count_sort(items):
    def get_min_max(items):
        min_ = max_ = items[0]

        for i in items:
            if i < min_:
                min_ = i
            if i > max_:
                max_ = i

        return min_, max_

    min, max = get_min_max(items)

    count_array = [0] * (max - min + 1)

    offset = abs(min) if min < 0 else 0

    for i in items:
        count_array[i + offset] += 1

    result = []

    for i, v in enumerate(count_array):
        if v > 0:
            result = result + ([i - offset] * v)

    return result


def get_numbers():
    return [3, 8, 1, -4, 0, 20, -15, 7, -4, 8, 8]


expected = [-15, -4, -4, 0, 1, 3, 7, 8, 8, 8, 20]

algs = [
    bubble_sort,
    selection_sort,
    insertion_sort,
    count_sort
]

for alg in algs:
    print(alg(get_numbers()) == expected)

numbers = get_numbers()
quick_sort(numbers, 0, len(numbers) - 1)
print(numbers == expected)

numbers = get_numbers()
merge_sort(numbers)
print(numbers == expected)
