# Binary search: First and last indexes

def first_and_last_index(arr, number):
    # search first occurence
    first_index = find_start_index(arr, number, 0, len(arr) - 1)

    # search last occurence
    last_index = find_end_index(arr, number, 0, len(arr) - 1)
    return [first_index, last_index]


def find_start_index(arr, number, start_index, end_index):
    # binary search solution to search for the first index of the array
    if start_index > end_index:
        return -1

    mid_index = start_index + (end_index - start_index)//2

    if arr[mid_index] == number:
        current_start_pos = find_start_index(
            arr, number, start_index, mid_index - 1)
        if current_start_pos != -1:
            start_pos = current_start_pos
        else:
            start_pos = mid_index
        return start_pos

    elif arr[mid_index] < number:
        return find_start_index(arr, number, mid_index + 1, end_index)
    else:
        return find_start_index(arr, number, start_index, mid_index - 1)


def find_end_index(arr, number, start_index, end_index):
    # binary search solution to search for the last index of the array
    if start_index > end_index:
        return -1

    mid_index = start_index + (end_index - start_index)//2

    if arr[mid_index] == number:
        current_end_pos = find_end_index(arr, number, mid_index + 1, end_index)
        if current_end_pos != -1:
            end_pos = current_end_pos
        else:
            end_pos = mid_index
        return end_pos
    elif arr[mid_index] < number:
        return find_end_index(arr, number, mid_index + 1, end_index)
    else:
        return find_end_index(arr, number, start_index, mid_index - 1)


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    solution = test_case[2]
    output = first_and_last_index(input_list, number)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


input_list = [1]
number = 1
solution = [0, 0]
test_case_1 = [input_list, number, solution]
test_function(test_case_1)

input_list = [0, 1, 2, 3, 3, 3, 3, 4, 5, 6]
number = 3
solution = [3, 6]
test_case_2 = [input_list, number, solution]
test_function(test_case_2)

input_list = [0, 1, 2, 3, 4, 5]
number = 5
solution = [5, 5]
test_case_3 = [input_list, number, solution]
test_function(test_case_3)

input_list = [0, 1, 2, 3, 4, 5]
number = 6
solution = [-1, -1]
test_case_4 = [input_list, number, solution]
test_function(test_case_4)
