# Reversing array in place
def reverse(items):
    i = 0
    j = len(items) - 1

    while i < j:
        swap(items, i, j)
        i += 1
        j -= 1


def swap(items, index_1, index_2):
    items[index_1], items[index_2] = items[index_2], items[index_1]

    return items


case_1 = [1, 2, 3, 4, 5, 6]
expected_1 = [6, 5, 4, 3, 2, 1]

case_2 = [1, 2, 3, 4, 5]
expected_2 = [5, 4, 3, 2, 1]

reverse(case_1)
print(case_1 == expected_1)

reverse(case_2)
print(case_2 == expected_2)
