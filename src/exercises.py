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


# Palindrome problem
def is_palindrome(word):
    i = 0
    j = len(word) - 1

    while i < j:
        if word[i] != word[j]:
            return False

        i += 1
        j -= 1

    return True


palindrome = 'aabcccbaa'
not_palindrome = 'aabccbbaa'

print(is_palindrome(palindrome) is True)
print(is_palindrome(not_palindrome) is False)


# Reverse integer problem
def reverse_int(number):
    reversed = 0
    while number > 0:
        rem = number % 10
        number //= 10
        reversed = reversed * 10 + rem

    return reversed


n_1 = 123045
n_2 = 1000000
n_3 = 1
n_4 = 0

print(reverse_int(n_1) == 540321)
print(reverse_int(n_2) == 1)
print(reverse_int(n_3) == 1)
print(reverse_int(n_4) == 0)


# Duplicates in array problem
# find duplicates in a one-dimensional array of integers in O(N) running time where: 0 < the integer values < length of the array
def get_duplicate(arr):
    for i in arr:
        if arr[abs(i)] >= 0:
            arr[abs(i)] *= -1
        else:
            print(f'Duplicate: {abs(i)}')


dups = [1, 2, 4, 3, 1, 2]
no_dups = [0, 1, 2, 3, 4, 5]

# Expected duplicates: 1, 2
get_duplicate(dups)

# Expected duplicates: None
get_duplicate(no_dups)


# Anagram problem
def is_anagram(word_1, word_2):
    if len(word_1) != len(word_2):
        return False

    return sorted(word_1) == sorted(word_2)


subject = 'dupa'
anagram = 'upad'
not_anagram = 'upal'

print(is_anagram(subject, anagram) is True)
print(is_anagram(subject, not_anagram) is False)


# Largest sum of subarray in O(N) time complexity
def subarray_with_largest_sum(arr):
    start = end = None
    max_ = arr[0]
    sum_ = 0
    biggest = [0, start, end]

    for i in range(len(arr)):
        if arr[i] > max_:
            max_ = arr[i]

        if start is None:
            if arr[i] <= 0:
                continue
            start = i

        end = i
        sum_ += arr[i]

        if sum_ > biggest[0]:
            biggest = [sum_, start, end]

        elif sum_ > 0:
            continue
        else:
            start = end = None
            sum_ = 0

    if max_ > biggest[0]:
        return [max_]
    return arr[biggest[1]:biggest[2] + 1]


numbers = [15, 10, -50, 12, -3, 0, 8, 10, -10]
print(subarray_with_largest_sum(numbers) == [12, -3, 0, 8, 10])


def largest_sum(arr):
    sum_ = 0
    biggest = 0

    for i in arr:
        sum_ = max(i, sum_ + i)
        biggest = max(sum_, biggest)

    return biggest


print(largest_sum(numbers) == 27)
