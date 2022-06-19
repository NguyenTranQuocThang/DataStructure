

# ->
# def push(self, value):
#         new_node = Node(value)
#         # if stack is empty
#         if self.head is None:
#             self.head = new_node
#         # Should we add it to the tail?
#         else:
#             current_node = head
#             while current_node.next:
#                 current_node = current_node.next
#             current_node.next = new_node
#         # Or should we add it to the head?
#         else:
#             new_node.next = self.head    # place the new node at the head of the linked list (top)
#             self.head = new_node

#         self.num_elements += 1

# if u add to tail after each of push u will loop every push -> performance decrease

# -> so add to tail

# Now give it a try for yourself. In the cell below, add the push method:

# The method will need to have a parameter for the value that you want to push
# You'll then need to create a new Node object with this value and link it to the list
# Remember that we want to add new items at the head of the stack, not the tail!
# Once you've added the new node, you'll want to increment num_elements

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:

    def __init__(self):
        self.head = None
        self.num_elements = 0

    # TODO: Add the push method

    def push(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.num_elements += 1
