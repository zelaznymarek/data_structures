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


def get_numbers():
    return [3, 8, 1, -4, 0, 20, -15, 7]


expected = [-15, -4, 0, 1, 3, 7, 8, 20]

algs = [
    bubble_sort,
    selection_sort,
    insertion_sort
]

for alg in algs:
    print(alg(get_numbers()) == expected)

numbers = get_numbers()
quick_sort(numbers, 0, len(numbers) - 1)
print(numbers == expected)
