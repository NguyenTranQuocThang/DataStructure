class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

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
