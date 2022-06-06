class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self, head=None):  # <-- Expects "head" to be a Node made up of an int or LinkedList
        self.head = head

    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next

    def __repr__(self):
        return str([v for v in self])

# Define a function outside of the class


def prepend(self, value):
    if self.head is None:
        self.head = Node(value)
        return
    new_head = Node(value)
    new_head.next = self.head
    self.head = new_head
    return


# This is the way to add a function to a class after it has been defined
LinkedList.prepend = prepend

# Test prepend
linked_list = LinkedList()
linked_list.prepend(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"


def append(self, value):
    if self.head is None:
        head = Node(value)
        self.head = head
        return
    current = self.head
    while current.next:
        current = current.next
    current.next = Node(value)
    return


LinkedList.append = append
# Test append - 1
linked_list.append(3)

linked_list.prepend(2)


assert linked_list.to_list() == [
    2, 1, 3], f"list contents: {linked_list.to_list()}"
# Test append - 2
linked_list = LinkedList()
linked_list.append(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
linked_list.append(3)
assert linked_list.to_list() == [
    1, 3], f"list contents: {linked_list.to_list()}"


def search(self, value):
    """ Search the linked list for a node with the requested value and return the node. """
    # TODO: Write function to search here
    head = self.head
    while head:
        if head.value == value:
            return head
        head = head.next
    return


LinkedList.search = search

# Test search
linked_list.prepend(2)
linked_list.prepend(1)
linked_list.append(4)
linked_list.append(3)
assert linked_list.search(
    1).value == 1, f"list contents: {linked_list.to_list()}"
assert linked_list.search(
    4).value == 4, f"list contents: {linked_list.to_list()}"


def remove(self, value):
    """ Remove first occurrence of value. """
    # TODO: Write function to remove here
    if self.head is None:
        return
    if self.head.value == value:
        self.head = self.head.next
        return
    node = self.head
    while node.next:
        if node.next.value == value:
            node.next = node.next.next
            return
        node = node.next


LinkedList.remove = remove

# Test remove
linked_list.remove(1)

assert linked_list.to_list() == [2, 1, 3, 4,
                                 3], f"list contents: {linked_list.to_list()}"


linked_list.remove(3)

assert linked_list.to_list() == [
    2, 1, 4, 3], f"list contents: {linked_list.to_list()}"


linked_list.remove(3)
assert linked_list.to_list() == [
    2, 1, 4], f"list contents: {linked_list.to_list()}"


def pop(self):
    if self.head is None:
        return
    data = self.head
    self.head = data.next
    return data.value


LinkedList.pop = pop

# Test pop
value = linked_list.pop()
assert value == 2, f"list contents: {linked_list.to_list()}"
assert linked_list.head.value == 1, f"list contents: {linked_list.to_list()}"


def insert(self, value, pos):
    if self.head is None:
        self.head = Node(value)
        return
    if pos == 0:
        linked_list.prepend(value)
        return
    index = 0
    node = self.head
    while node.next:
        if(pos == index + 1):
            new_node = Node(value)
            new_node.next = node.next
            node.next = new_node
            return
        node = node.next
        index += 1
    self.append(value)


LinkedList.insert = insert

# Test insert
linked_list.insert(5, 0)
assert linked_list.to_list() == [
    5, 1, 4], f"list contents: {linked_list.to_list()}"
linked_list.insert(2, 1)
assert linked_list.to_list() == [
    5, 2, 1, 4], f"list contents: {linked_list.to_list()}"
linked_list.insert(3, 6)
assert linked_list.to_list() == [5, 2, 1, 4,
                                 3], f"list contents: {linked_list.to_list()}"


def size(self):
    size = 0
    head = self.head
    while head:
        size += 1
        head = head.next
    return size


LinkedList.size = size

# Test size function
assert linked_list.size() == 5, f"list contents: {linked_list.to_list()}"


def reverse(linked_list):
    """
    Reverse the inputted linked list

    Args:
       linked_list(obj): Linked List to be reversed
    Returns:
       obj: Reveresed Linked List
    """
    # TODO: Write your function to reverse linked lists here
    new_list = LinkedList()
    previous_node = None
    for i in linked_list:
        head = Node(i)
        head.next = previous_node
        previous_node = head
    new_list.head = previous_node
    return new_list


llist = LinkedList()

for value in [4, 2, 5, 1, -3, 0]:
    llist.append(value)

flipped = reverse(llist)
is_correct = list(flipped) == list(
    [0, -3, 1, 5, 2, 4]) and list(llist) == list(reverse(flipped))
print("Pass" if is_correct else "Fail")


# -------------------------------------------------- Falltten a Nested Linked List
print("\n-------------------Falltten a Nested Linked List-------------------\n")


def append(self, value):

    # If LinkedList is empty
    if self.head is None:
        self.head = Node(value)
        return

        # Create a temporary Node object
    node = self.head

    # Iterate till the end of the currrent LinkedList
    while node.next is not None:
        node = node.next
    # Append the newly creataed Node at the end of the currrent LinkedList
    node.next = Node(value)


LinkedList.append = append

'''We will need this function to convert a LinkedList object into a Python list of integers'''


def to_list(self):
    out = []          # <-- Declare a Python list
    node = self.head  # <-- Create a temporary Node object

    while node:       # <-- Iterate untill we have nodes available
        # <-- node.value is actually of type Node, therefore convert it into int before appending to the Python list
        out.append(int(str(node.value)))
        node = node.next

    return out


LinkedList.to_list = to_list


def merge(list1, list2):
    merged = LinkedList(None)
    if list1 is None:
        return list2
    if list2 is None:
        return list1
    list1_elt = list1.head
    list2_elt = list2.head
    while list1_elt is not None or list2_elt is not None:
        if list1_elt is None:
            merged.append(list2_elt)
            list2_elt = list2_elt.next
        elif list2_elt is None:
            merged.append(list1_elt)
            list1_elt = list1_elt.next
        elif list1_elt.value <= list2_elt.value:
            merged.append(list1_elt)
            list1_elt = list1_elt.next
        else:
            merged.append(list2_elt)
            list2_elt = list2_elt.next
    return merged


''' In a NESTED LinkedList object, each node will be a simple LinkedList in itself'''


''' In a NESTED LinkedList object, each node will be a simple LinkedList in itself'''


class NestedLinkedList(LinkedList):
    def flatten(self):
        # <-- self.head is a node for NestedLinkedList
        return self._flatten(self.head)

    '''  A recursive function '''

    def _flatten(self, node):

        # A termination condition
        if node.next is None:
            # <-- First argument is a simple LinkedList
            return merge(node.value, None)

        # _flatten() is calling itself untill a termination condition is achieved
        # <-- Both arguments are a simple LinkedList each
        return merge(node.value, self._flatten(node.next))


''' Test merge() function'''
linked_list = LinkedList(Node(1))
linked_list.append(3)
linked_list.append(5)

second_linked_list = LinkedList(Node(2))
second_linked_list.append(4)

merged = merge(linked_list, second_linked_list)
node = merged.head
while node is not None:
    # This will print 1 2 3 4 5
    print(node.value)
    node = node.next

# Lets make sure it works with a None list
merged = merge(None, linked_list)
node = merged.head
while node is not None:
    # This will print 1 3 5
    print(node.value)
    node = node.next

''' Test flatten() function'''
# Create a nested linked list with one node.
# The node itself is a simple linked list as 1-->3-->5 created previously
nested_linked_list = NestedLinkedList(Node(linked_list))

# Append a node (a linked list as 2-->4) to the existing nested linked list
nested_linked_list.append(second_linked_list)

# Call the flatten() function
flattened = nested_linked_list.flatten()

# Logic to print the flattened list
node = flattened.head
while node is not None:
    # This will print 1 2 3 4 5
    print(node.value)
    node = node.next

# -------------------------------------------------- Sorting linked lists
print("\n-------------------Sorting linked list-------------------\n")


class SortedLinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next

    def __repr__(self):
        return str([v for v in self])

    # def append(self, value):
    #     """
    #     Append a value to the Linked List in ascending sorted order

    #     Args:
    #        value(int): Value to add to Linked List
    #     """

    #     # TODO: Write your sorted append function here

    #     # pass
    #     head = self.head
    #     if head == None:
    #         self.head = Node(value)
    #         return
    #     if self.head.value > value:
    #         new_node = Node(value)
    #         new_node.next = head.next
    #         self.head = new_node
    #         return
    #     while head.next:
    #         if head.value > value:
    #             new_node = Node(value)
    #             new_node.next = head.next
    #             head.next = new_node
    #             return
    #         head = head.next
    def append(self, value):
        """
        Append a value to the Linked List in ascending sorted order

        Args:
           value(int): Value to add to Linked List
        """
        if self.head is None:
            self.head = Node(value)
            return

        if value < self.head.value:
            node = Node(value)
            node.next = self.head
            self.head = node
            return

        node = self.head
        while node.next is not None and value >= node.next.value:
            node = node.next

        new_node = Node(value)
        new_node.next = node.next
        node.next = new_node

        return None


# Test cases
linked_list = SortedLinkedList()
linked_list.append(3)
print("Pass" if (linked_list.head.value == 3) else "Fail")

linked_list.append(2)
print("Pass" if (linked_list.head.value == 2) else "Fail")

linked_list.append(4)


node = linked_list.head.next.next
print("Pass" if (node.value == 4) else "Fail")

# -------------------------- Loops detecting (circle linked list)
print("\n------------------------ Loops detecting --------------------------\n")


class LinkedListCircle:
    def __init__(self, init_list=None):
        self.head = None
        if init_list:
            for value in init_list:
                self.append(value)

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        # Move to the tail (the last node)
        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)
        return


list_with_loop = LinkedListCircle([2, -1, 3, 0, 5])

# Creating a loop where the last node points back to the second node
loop_start = list_with_loop.head.next

node = list_with_loop.head
while node.next:
    node = node.next
node.next = loop_start


def iscircular(linked_list):
    """
    Determine whether the Linked List is circular or not

    Args:
       linked_list(obj): Linked List to be checked
    Returns:
       bool: Return True if the linked list is circular, return False otherwise
    """

    # TODO: Write function to check if linked list is circular

    # pass

    if linked_list.head is None:
        return False

    slow = linked_list.head
    fast = linked_list.head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
        return False

# Test Cases


# Create another circular linked list
small_loop = LinkedListCircle([0])
small_loop.head.next = small_loop.head

# Pass  /// something wrong here :> but i'm not fix that
print("Pass" if iscircular(list_with_loop) else "Fail")
print("Pass" if iscircular(LinkedListCircle(
    [-4, 7, 2, 5, -1])) else "Fail")   # Fail
print("Pass" if iscircular(LinkedListCircle(
    [1])) else "Fail")                 # Fail
print("Pass" if iscircular(small_loop) else "Fail")                      # Pass
print("Pass" if iscircular(LinkedListCircle([]))
      else "Fail")                  # Fail

# ---------------------------------- Add one ---------------------------------------
print("-------------------------------- Add one -------------------------------------")

# def add_one(arr):
#     add = 1
#     for i in range(len(arr)-1 , -1 , -1):
#         number = add + arr[i]
#         if number != 10:
#             arr[i] = number
#             return arr
#         else:
#             arr[i] = 0
#     return [add] + arr


def add_one(arr):
    add = 1
    for i in range(len(arr) - 1, -1, -1):
        number = add + arr[i]
        add = number // 10
        if add == 0:
            arr[i] = number
            return arr
        else:
            arr[i] = number % 10
    return [add] + arr

# A helper function for Test Cases


def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]

    output = add_one(arr)
    print(output)
    for index, element in enumerate(output):
        if element != solution[index]:
            print("Fail")
            return
    print("Pass")


# Test Case 3
arr = [9, 9, 9]
solution = [1, 0, 0, 0]
test_case = [arr, solution]
test_function(test_case)

# ----------------------------------- Max sum sub-array  ----------------------------------------

print("-------------------------- Max sum sub-array -----------------------------")

# Solution
'''
The Idea:
1. We have to find the sum of "contiguous" subarray, therefore we must not change the order of array elements.
2. Let current_sum denotes the sum of a subarray, and max_sum denotes the maximum value of current_sum.
3. LOOP STARTS: For each element of the array, update the current_sum with the MAXIMUM of either:
 - The element added to the current_sum (denotes the addition of the element to the current subarray)
 - The element itself  (denotes the starting of a new subarray)
 - Update (overwrite) max_sum, if it is lower than the updated current_sum
4. Return max_sum
'''


# def max_sum_subarray(arr):

#     current_sum = arr[0]  # current_sum denotes the sum of a subarray
#     # max_sum denotes the maximum value of current_sum ever
#     max_sum = arr[0]

#     # Loop from VALUE at index position 1 till the end of the array
#     for element in arr[1:]:

#         '''
#         # Compare (current_sum + element) vs (element)
#         # If (current_sum + element) is higher, it denotes the addition of the element to the current subarray
#         # If (element) alone is higher, it denotes the starting of a new subarray
#         '''
#         current_sum = max(current_sum + element, element)

#         # Update (overwrite) max_sum, if it is lower than the updated current_sum
#         max_sum = max(current_sum, max_sum)

#     return max_sum

def max_sum_subarray(arr):
    max_sum = arr[0]
    sub_sum = arr[0]
    for i in arr[1:]:
        sub_sum += i
        sub_sum = max(sub_sum, i)
        max_sum = max(sub_sum, max_sum)
    return max_sum


def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]

    output = max_sum_subarray(arr)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


arr = [1, 2, 3, -4, 6]
solution = 8  # sum of array

test_case = [arr, solution]
test_function(test_case)
arr = [1, 2, -5, -4, 1, 6]
solution = 7   # sum of last two elements

test_case = [arr, solution]
test_function(test_case)
arr = [-12, 15, -13, 14, -1, 2, 1, -5, 4]
solution = 18  # sum of subarray = [15, -13, 14, -1, 2, 1]

test_case = [arr, solution]
test_function(test_case)


# ---------------------------- max_sum_subarray ---------------------------------------
print("------------------------- max_sum_subarray -------------------------")

# Solution
'''
The Idea:
1. We have to find the sum of "contiguous" subarray, therefore we must not change the order of array elements.
2. Let current_sum denotes the sum of a subarray, and max_sum denotes the maximum value of current_sum.
3. LOOP STARTS: For each element of the array, update the current_sum with the MAXIMUM of either:
 - The element added to the current_sum (denotes the addition of the element to the current subarray)
 - The element itself  (denotes the starting of a new subarray)
 - Update (overwrite) max_sum, if it is lower than the updated current_sum
4. Return max_sum
'''


def max_sum_subarray(arr):

    current_sum = arr[0]  # current_sum denotes the sum of a subarray
    # max_sum denotes the maximum value of current_sum ever
    max_sum = arr[0]

    # Loop from VALUE at index position 1 till the end of the array
    for element in arr[1:]:

        '''
        # Compare (current_sum + element) vs (element)
        # If (current_sum + element) is higher, it denotes the addition of the element to the current subarray
        # If (element) alone is higher, it denotes the starting of a new subarray
        '''
        current_sum = max(current_sum + element, element)

        # Update (overwrite) max_sum, if it is lower than the updated current_sum
        max_sum = max(current_sum, max_sum)

    return max_sum


def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]

    output = max_sum_subarray(arr)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


arr = [1, 2, 3, -4, 6]
solution = 8  # sum of array

test_case = [arr, solution]
test_function(test_case)
arr = [1, 2, -5, -4, 1, 6]
solution = 7   # sum of last two elements

test_case = [arr, solution]
test_function(test_case)
arr = [-12, 15, -13, 14, -1, 2, 1, -5, 4]
solution = 18  # sum of subarray = [15, -13, 14, -1, 2, 1]

test_case = [arr, solution]
test_function(test_case)

# ---------------------------------------- Pascal Triangle  ----------------------------------------
print("------------------------ Pascal Triangle ----------------------------")


# Solution

'''
Points to note:
1. We have to return a list.
2. The elements of n^th row are made up of elements of (n-1)^th row. This comes up till the 1^st row. We will follow a top-down approach. 
3. Except for the first and last element, any other element at position j in the current row is the sum of elements at position j and j-1 in the previous row. 
4. Be careful about the edge cases, example, an index should never be a NEGATIVE at any point of time. 
'''


# def nth_row_pascal(n):

#     if n == 0:
#         return [1]

#     current_row = [1]  # First row

#     ''' Loop from 1 to n; i denotes the row number'''
#     for i in range(1, n + 1):
#         # Set the current_row from previous iteration as the previous_row
#         previous_row = current_row

#         # Let's build the fresh current_row gradually
#         # add the default first element at the 0^th index of the i^th row
#         current_row = [1]

#         '''Loop from 1 to (i-1); j denotes the index of an element with in the i^th row'''
#         # Example, for 5th row we have considered n=4,
#         # we will iterate index from 1 to 3, because
#         # the default element at the 0^th index has already been added
#         for j in range(1, i):

#             # An element at position j in the current row is the
#             # sum of elements at position j and j-1 in the previous row.
#             next_number = previous_row[j] + previous_row[j - 1]

#             # Append the new element to the current_row
#             current_row.append(next_number)

#         current_row.append(1)  # append the default last element
#     return current_row

def nth_row_pascal(n):
    if n == 0:
        return [1]
    current_row = [1]
    for i in range(1, n + 1):
        previous_row = current_row
        current_row = [1]
        for j in range(1, i):
            number = previous_row[j] + previous_row[j-1]
            current_row.append(number)
        current_row.append(1)
    return current_row


def test_function(test_case):
    n = test_case[0]
    solution = test_case[1]
    output = nth_row_pascal(n)
    if solution == output:
        print("Pass")
    else:
        print("Fail")


n = 0
solution = [1]

test_case = [n, solution]
test_function(test_case)
n = 1
solution = [1, 1]

test_case = [n, solution]
test_function(test_case)
n = 2
solution = [1, 2, 1]

test_case = [n, solution]
test_function(test_case)
n = 3
solution = [1, 3, 3, 1]

test_case = [n, solution]
test_function(test_case)
n = 4
solution = [1, 4, 6, 4, 1]

test_case = [n, solution]
test_function(test_case)
