# Iterative solution
print("-----------------------------------------------------------------------Iterative solution------------------------------------------------------------------------")


def binary_search(array, target):
    '''Write a function that implements the binary search algorithm using iteration

    args:
      array: a sorted array of items of the same type
      target: the element you're searching for

    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    '''

    start_index = 0
    end_index = len(array) - 1
    while(start_index <= end_index):
        middle_index = (start_index + end_index) // 2
        if(array[middle_index] == target):
            return middle_index
        elif(array[middle_index] > target):
            end_index = middle_index - 1
        else:
            start_index = middle_index + 1
    return -1
    # pass


def test_function(test_case):
    answer = binary_search(test_case[0], test_case[1])
    if answer == test_case[2]:
        print("Pass!")
    else:
        print("Fail!")


array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 6
index = 6
test_case = [array, target, index]
test_function(test_case)


print("-----------------------------------------------------------------------Recursive solution------------------------------------------------------------------------")


def binary_search_recursive(array, target):
    '''
    This function will call binary_search_recursive_soln function.
    You don't need to change this function.

    args:
      array: a sorted array of items of the same type
      target: the element you're searching for
    '''
    return binary_search_recursive_soln(array, target, 0, len(array) - 1)


def binary_search_recursive_soln(array, target, start_index, end_index):
    '''Write a function that implements the binary search algorithm using recursion

    args:
      array: a sorted array of items of the same type
      target: the element you're searching for
      start_index: beginning of the index of the sub-arrays
      end_index: end of the index of the sub-arrays

    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    '''

    middle_index = (start_index + end_index) // 2

    if array[middle_index] == target:
        return middle_index
    elif(array[middle_index] > target):
        return binary_search_recursive_soln(array, target, start_index, middle_index - 1)
    else:
        return binary_search_recursive_soln(array, target, middle_index + 1, end_index)
        # pass


def test_function(test_case):
    answer = binary_search_recursive(test_case[0], test_case[1])
    if answer == test_case[2]:
        print("Pass!")
    else:
        print("Fail!")


array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 4
index = 4
test_case = [array, target, index]
test_function(test_case)
print("-----------------------------------------------------------------------Another solution------------------------------------------------------------------------")

# difference way


def recursive_binary_search(target, source, left=0):
    if len(source) == 0:
        return None
    center = (len(source)-1) // 2
    if source[center] == target:
        return center + left
    elif source[center] < target:
        return recursive_binary_search(target, source[center+1:], left+center+1)
    else:
        return recursive_binary_search(target, source[:center], left)


multiple = [1, 3, 5, 7, 7, 7, 8, 11, 12]
print(recursive_binary_search(7, multiple))

print("-----------------------------------------------------------------------Search first element position solution------------------------------------------------------------------------")

# if i want to search first element position


def find_first(target, source):
    index = recursive_binary_search(target, source)
    if not index:
        return None
    while source[index] == target:
        if index == 0:
            return 0
        if source[index-1] == target:
            index -= 1
        else:
            return index


multiple = [1, 3, 5, 7, 7, 7, 8, 11, 12, 13, 14, 15]
print(find_first(7, multiple))  # Should return 3
print(find_first(9, multiple))  # Should return None


print("-----------------------------------------------------------------------Check contain element solution------------------------------------------------------------------------")


print("-----------------------------------------------------------------------First way solution------------------------------------------------------------------------")
# Native implementation of binary search in the contains function.


def contains(target, source):
    if len(source) == 0:
        return False
    center = (len(source)-1) // 2
    if source[center] == target:
        return True
    elif source[center] < target:
        return contains(target, source[center+1:])
    else:
        return contains(target, source[:center])


letters = ['a', 'c', 'd', 'f', 'g']
print(contains('c', letters))  # True
print(contains('b', letters))  # False
print("-----------------------------------------------------------------------Second way solution------------------------------------------------------------------------")
# Loose wrapper for recursive binary search, returning True if the index is found and False if not


def contains(target, source):
    return recursive_binary_search(target, source) is not None


letters = ['a', 'c', 'd', 'f', 'g']
print(contains('a', letters))  # True
print(contains('b', letters))  # False
