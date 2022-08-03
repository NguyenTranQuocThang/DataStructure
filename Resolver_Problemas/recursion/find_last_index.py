def last_index(arr, target):
    """
    :param: arr - input array
    :param: target - integer element
    return: int - last index of target in arr
    #TODO: complete this method to find the last index of target in arr
    """
    # pass
    return find_index(arr, target, -1)


def find_index(arr, target, locate):
    if not arr:
        print(locate)
        return locate
    las_element = arr[-1]
    if las_element == target:
        locate = len(arr)
    find_index(arr[:-1], target, locate)


def test_function(test_case):
    arr = test_case[0]
    target = test_case[1]
    solution = test_case[2]
    output = last_index(arr, target)
    if output == solution:
        print("Pass")
    else:
        print("FAIL: Expected", solution, ", but you've got:", output)


arr = [1, 2, 5, 5, 4]
target = 5
solution = 3

test_case = [arr, target, solution]
test_function(test_case)
arr = [1, 2, 5, 5, 4]
target = 7
solution = -1

test_case = [arr, target, solution]
test_function(test_case)
arr = [91, 19, 3, 8, 9]
target = 91
solution = 0

test_case = [arr, target, solution]
test_function(test_case)
arr = [1, 1, 1, 1, 1, 1]
target = 1
solution = 5

test_case = [arr, target, solution]
test_function(test_case)
