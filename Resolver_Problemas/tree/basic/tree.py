# this code makes the tree that we'll traverse

class Node(object):

    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    # set value of the node
    def set_value(self, value):
        self.value = value

    # get value of the node
    def get_value(self):
        return self.value

    # set a node for the left child
    def set_left_child(self, left):
        self.left = left

    # set a node for the right child
    def set_right_child(self, right):
        self.right = right

    # get the node of left child
    def get_left_child(self):
        return self.left

    # get the node of right child
    def get_right_child(self):
        return self.right

    # check if node has left child -> return boolean
    def has_left_child(self):
        return self.left != None

    # check if node has right child -> return boolean
    def has_right_child(self):
        return self.right != None

    # define _repr to decide what a print statement displays for a Node object
    def __repr__(self):
        return f"Node({self.get_value()})"

    def __str__(self):
        return f"Node({self.get_value()})"


class Tree():
    def __init__(self, value=None):
        self.root = Node(value)

    def get_root(self):
        return self.root


# create a tree and add some nodes
tree = Tree("apple")  # root node

# set first level's left child
tree.get_root().set_left_child(Node("banana"))

# set first level's right child
tree.get_root().set_right_child(Node("cherry"))

# set second level's left child
# by getting the first level's left child first
tree.get_root().get_left_child().set_left_child(Node("dates"))
