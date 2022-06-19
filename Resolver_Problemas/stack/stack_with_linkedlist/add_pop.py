class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:

    def __init__(self):
        self.head = None
        self.num_elements = 0

    def push(self, value):
        new_node = Node(value)
        # if stack is empty
        if self.head is None:
            self.head = new_node
        else:
            # place the new node at the head (top) of the linked list
            new_node.next = self.head
            self.head = new_node

        self.num_elements += 1

    # TODO: Add the pop method
    def pop(self):
        if self.head is None:
            return None
        else:
            pop_node = self.head
            self.head = pop_node.next
            self.num_elements -= 1
            return pop_node.value

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0
