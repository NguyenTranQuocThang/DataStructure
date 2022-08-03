# this code makes the tree that we'll traverse

from numpy import rec


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

# Let's define a stack to help keep track of the tree nodes


class Stack():
    def __init__(self):
        self.list = list()

    # add an element to the list
    def push(self, value):
        self.list.append(value)

    # remove the last element from the list
    def pop(self):
        return self.list.pop()

    # get the value of the last element in the list
    def top(self):
        if len(self.list) > 0:
            return self.list[-1]
        else:
            return None

    # check if the list empty
    def is_empty(self):
        return len(self.list) == 0

    #
    def __repr__(self):
        if len(self.list) > 0:
            s = "<top of stack>\n_________________\n"
            s += "\n_________________\n".join([str(item)
                                              for item in self.list[::-1]])
            s += "\n_________________\n<bottom of stack>"
            return s

        else:
            return "<stack is empty>"


# instantiate Stack
stack = Stack()
# add elements into the stack
stack.push("apple")
stack.push("banana")
stack.push("cherry")
stack.push("dates")
# remove and print the last element (top of the stack)
print(stack.pop())
print("\n")
print(stack)

# code
visit_order = list()
stack = Stack()
# start at the roor node, visit it and then add it to the stack
node = tree.get_root()
stack.push(node)
print(f"""
visit_order {visit_order} 
stack:
{stack}
""")
# visit apple (root)
visit_order.append(node.get_value())
print(f"""
visit_order {visit_order} 
stack:
{stack}
""")
# check if apple (root) has a left child
print(f"{node} has left child? {node.has_left_child()}")

# since apple has a left child (banana)
# we'll visit banana and add it to the stack
if node.has_left_child():
    node = node.get_left_child()
    stack.push(node)

print(f"""
visit_order {visit_order} 
stack:
{stack}
""")
# check if banana has a left child (second level's left chile)
print(f"{node} has left child? {node.has_left_child()}")

# since banana has a left child "dates"
# we'll visit "dates" and add it to the stack
if node.has_left_child():
    node = node.get_left_child()
    stack.push(node)

print(f"""
visit_order {visit_order} 
stack:
{stack}
""")
# visit banana (first level's left child)
print(f"visit {node}")
visit_order.append(node.get_value())
print(f"""visit_order {visit_order}""")
# check if banana has a left child (second level's left chile)
print(f"{node} has left child? {node.has_left_child()}")

# since banana has a left child "dates"
# we'll visit "dates" and add it to the stack
if node.has_left_child():
    node = node.get_left_child()
    stack.push(node)

print(f"""
visit_order {visit_order} 
stack:
{stack}
""")
# visit dates (second level's left chile)
visit_order.append(node.get_value())
print(f"visit order {visit_order}")


# check if "dates" has a left child -> return boolean value
print(f"{node} has left child? {node.has_left_child()}")
# since dates doesn't have a left child, we'll check if it has a right child
print(f"{node} has right child? {node.has_right_child()}")
# since "dates" is a leaf node (has no children), we can start to retrace our steps
# in other words, we can pop it off the stack.
print(stack.pop())
print(stack)
# now we'll set the node to the new top of the stack, which is banana
node = stack.top()
print(node)
# we already checked for banana's left child, so we'll check for its right child
print(f"{node} has right child? {node.has_right_child()}")
# banana doesn't have a right child, so we're also done tracking it.
# so we can pop banana off the stack
print(f"pop {stack.pop()} off stack")
print(f"""
stack
{stack}
""")
# now we'll track the new top of the stack, which is apple
node = stack.top()
print(node)
# we've already checked if apple has a left child; we'll check if it has a right child
print(f"{node} has right child? {node.has_right_child()}")
# since it has a right child (cherry),
# we'll visit cherry and add it to the stack.
if node.has_right_child():
    node = node.get_right_child()
    stack.push(node)

print(f"""
visit_order {visit_order} 
stack
{stack}
""")
# visit cherry (first level's right child)
print(f"visit {node}")
visit_order.append(node.get_value())
print(f"""visit_order: {visit_order}""")
# Now we'll check if cherry (first level's right child) has a left child
print(f"{node} has left child? {node.has_left_child()}")

# it doesn't, so we'll check if it has a right child
print(f"{node} has right child? {node.has_right_child()}")
# since cherry has neither left nor right child nodes,
# we are done tracking it, and can pop it off the stack

print(f"pop {stack.pop()} off the stack")

print(f"""
visit_order {visit_order} 
stack
{stack}
""")
# now we're back to apple at the top of the stack.
# since we've already checked apple's left and right child nodes,
# we can pop apple off the stack

print(f"pop {stack.pop()} off stack")
print(f"pre-order traversal visited nodes in this order: {visit_order}")
print(f"""stack
{stack}""")

# use stack fucntion to visit tree


class State(object):
    def __init__(self, node):
        self.node = node
        self.visited_left = False
        self.visited_right = False

    def get_node(self):
        return self.node

    def get_visited_left(self):
        return self.visited_left

    def get_visited_right(self):
        return self.visited_right

    def set_visited_left(self):
        self.visited_left = True

    def set_visited_right(self):
        self.visited_right = True

    def __repr__(self):
        s = f"""{self.node}
visited_left: {self.visited_left}
visited_right: {self.visited_right}
        """
        return s


def pre_order_with_stack(tree, debug_mode=False):
    visit_order = list()
    stack = Stack()
    node = tree.get_root()
    visit_order.append(node.get_value())
    state = State(node)
    stack.push(state)
    count = 0
    while(node):
        if debug_mode:
            print(f"""
loop count: {count}
current node: {node}
stack:
{stack}
            """)
        count += 1
        if node.has_left_child() and not state.get_visited_left():
            state.set_visited_left()
            node = node.get_left_child()
            visit_order.append(node.get_value())
            state = State(node)
            stack.push(state)

        elif node.has_right_child() and not state.get_visited_right():
            state.set_visited_right()
            node = node.get_right_child()
            visit_order.append(node.get_value())
            state = State(node)

        else:
            stack.pop()
            if not stack.is_empty():
                state = stack.top()
                node = state.get_node()
            else:
                node = None

    if debug_mode:
        print(f"""
loop count: {count}
current node: {node}
stack:
{stack}
            """)
    return visit_order
# check pre-order traversal


pre_order_with_stack(tree, debug_mode=True)

# visit list by stack use recursive
print("-------------------------------------------------------------------")


def pre_order(tree):

    visit_order = list()

    def traverse(node):
        if node:
            # visit the node
            visit_order.append(node.get_value())

            # traverse left subtree
            traverse(node.get_left_child())

            # traverse right subtree
            traverse(node.get_right_child())

    traverse(tree.get_root())

    return visit_order


print(pre_order(tree))


# solution
def in_order(tree):

    visit_order = list()

    def traverse(node):
        if node:
            # traverse left subtree
            traverse(node.get_left_child())

            # visit node
            visit_order.append(node.get_value())

            # traverse right sub-tree
            traverse(node.get_right_child())

    traverse(tree.get_root())

    return visit_order
# solution


def post_order(tree):

    visit_order = list()

    def traverse(node):
        if node:
            # traverse left subtree
            traverse(node.get_left_child())

            # traverse right subtree
            traverse(node.get_right_child())

            # visit node
            visit_order.append(node.get_value())

    traverse(tree.get_root())

    return visit_order
