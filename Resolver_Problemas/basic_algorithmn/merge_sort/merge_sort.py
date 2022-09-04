
def mergesort(items):
    if len(items) <= 1:
        return items

    mid = len(items) // 2

    left = items[:mid]

    right = items[mid:]

    left = mergesort(left)

    right = mergesort(right)

    return merge(left, right)


def merge(left, right):
    merge = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merge.append(right[right_index])
            right_index += 1
        else:
            merge.append(left[left_index])
            left_index += 1

    merge += left[left_index:]
    merge += right[right_index:]
    return merge


test_list_1 = [8, 3, 1, 7, 0, 10, 2]
test_list_2 = [1, 0]
test_list_3 = [97, 98, 99]
print('{} to {}'.format(test_list_1, mergesort(test_list_1)))
print('{} to {}'.format(test_list_2, mergesort(test_list_2)))
print('{} to {}'.format(test_list_3, mergesort(test_list_3)))


# def merge(left, right):
#     merged = []
#     left_index = 0
#     right_index = 0

#     # Move through the lists until we have exhausted one
#     while left_index < len(left) and right_index < len(right):
#         # If left's item is larger, append right's item
#         # and increment the index
#         if left[left_index] > right[right_index]:
#             merged.append(right[right_index])
#             right_index += 1
#         # Otherwise, append left's item and increment
#         else:
#             merged.append(left[left_index])
#             left_index += 1

#     # Append any leftovers. Because we've broken from our while loop,
#     # we know at least one is empty, and the remaining:
#     # a) are already sorted
#     # b) all sort past our last element in merged
#     merged += left[left_index:]
#     merged += right[right_index:]

#     # return the ordered, merged list
#     return merged

# # Test this out
# merged = merge([1,3,7], [2,5,6])
# print(merged)
