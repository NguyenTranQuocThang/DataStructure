

# Another way

def deep_reverse(arr):
    if len(arr) == 0:
        return []
    first_element = arr[0]
    sub_list = deep_reverse(arr[1:])
    if type(first_element) is list:
        first_element = deep_reverse(first_element)
    sub_list.append(first_element)
    return sub_list

# def deep_reverse(arr):
#     if len(arr) < 1:
#         return arr
#     results = []
#     for i in arr[::-1]:
#         if type(i) is list:
#             i = deep_reverse(i)
#         results.append(i)
#     return results


def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]

    output = deep_reverse(arr)
    if output == solution:
        print("Pass")
    else:
        print("False")


arr = [1, 2, 3, 4, 5]
solution = [5, 4, 3, 2, 1]
test_case = [arr, solution]
# test_function(test_case)
arr = [1, 2, [3, 4, 5], 4, 5]
solution = [5, 4, [5, 4, 3], 2, 1]
test_case = [arr, solution]
test_function(test_case)
arr = [1, [2, 3, [4, [5, 6]]]]
solution = [[[[6, 5], 4], 3, 2], 1]
test_case = [arr, solution]
# test_function(test_case)
arr = [1, [2, 3], 4, [5, 6]]
solution = [[6, 5], 4, [3, 2], 1]
test_case = [arr, solution]
# test_function(test_case)
